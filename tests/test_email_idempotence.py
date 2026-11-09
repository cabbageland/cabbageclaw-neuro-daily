import importlib.util
import json
import multiprocessing
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("neuro_daily_email", ROOT / "neuro_daily_email.py")
email = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(email)
DAY = "2026-11-09"
RECIPIENTS = ["subscriber@example.invalid"]


def competing_sender(state_dir, start, outcomes):
    email.STATE_DIR = Path(state_dir)
    email.SEND_STATE_PATH = email.STATE_DIR / "email_send_state.json"

    def fake_delivery(messages):
        # Keep the critical section open so both senders contend for it.
        with (email.STATE_DIR / "deliveries.txt").open("a") as handle:
            handle.write("delivered\n")
        time.sleep(0.2)

    if not start.wait(5):
        outcomes.put("timeout")
        return
    with patch.object(email, "send_messages", side_effect=fake_delivery):
        try:
            email.send_once(DAY, RECIPIENTS, [])
            outcomes.put("sent")
        except ValueError as exc:
            outcomes.put("duplicate" if "Refusing duplicate" in str(exc) else str(exc))


class EmailIdempotenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.state_dir = Path(self.temp.name)
        for name, value in (
            ("STATE_DIR", self.state_dir),
            ("SEND_STATE_PATH", self.state_dir / "email_send_state.json"),
        ):
            patcher = patch.object(email, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_two_processes_deliver_only_once(self):
        context = multiprocessing.get_context("fork")
        start, outcomes = context.Event(), context.Queue()
        workers = [context.Process(target=competing_sender, args=(str(self.state_dir), start, outcomes)) for _ in range(2)]
        try:
            for worker in workers:
                worker.start()
            start.set()
            for worker in workers:
                worker.join(5)
                self.assertEqual(worker.exitcode, 0)
            self.assertCountEqual([outcomes.get(timeout=1) for _ in workers], ["sent", "duplicate"])
            self.assertEqual((self.state_dir / "deliveries.txt").read_text(), "delivered\n")
        finally:
            for worker in workers:
                if worker.is_alive():
                    worker.terminate()
                    worker.join()
            outcomes.close()

    def test_partial_or_uncertain_delivery_blocks_automatic_retry(self):
        with patch.object(email, "send_messages", side_effect=RuntimeError("simulated connection loss")) as send:
            with self.assertRaises(RuntimeError):
                email.send_once(DAY, RECIPIENTS, [])
            with self.assertRaisesRegex(ValueError, "delivery may be partial"):
                email.send_once(DAY, RECIPIENTS, [])
            self.assertEqual(send.call_count, 1)
        self.assertEqual(email.load_send_state()["production"][DAY]["status"], "sending")

    def test_existing_legacy_success_blocks_delivery_without_network(self):
        email.save_send_state({"production": {DAY: {"sent_at": "2026-11-09T07:30:52", "recipient_count": 10}}})
        with patch.object(email, "send_messages") as send:
            with self.assertRaisesRegex(ValueError, "Refusing duplicate"):
                email.send_once(DAY, RECIPIENTS, [])
            send.assert_not_called()

    def test_corrupt_state_fails_closed(self):
        for contents in ("{", "[]", '{"production": []}', '{"production": {"2026-11-09": {}}}'):
            with self.subTest(contents=contents):
                email.SEND_STATE_PATH.write_text(contents)
                with patch.object(email, "send_messages") as send:
                    with self.assertRaisesRegex(ValueError, "state is unreadable"):
                        email.send_once(DAY, RECIPIENTS, [])
                    send.assert_not_called()
                self.assertEqual(email.SEND_STATE_PATH.read_text(), contents)

    def test_failed_atomic_replace_preserves_previous_state(self):
        email.save_send_state({"production": {DAY: {"recipient_count": 10}}})
        before = email.SEND_STATE_PATH.read_bytes()
        with patch.object(email.os, "replace", side_effect=OSError("simulated disk failure")):
            with self.assertRaises(OSError):
                email.save_send_state({})
        self.assertEqual(email.SEND_STATE_PATH.read_bytes(), before)
        self.assertEqual(list(self.state_dir.iterdir()), [email.SEND_STATE_PATH])

    def test_success_is_private_and_modes_remain_separate(self):
        with patch.object(email, "send_messages") as send:
            email.send_once(DAY, RECIPIENTS, [])
            email.send_once(DAY, RECIPIENTS, [], internal_test=True)
            self.assertEqual(send.call_count, 2)
        state = email.load_send_state()
        for mode in ("production", "internal_test"):
            self.assertEqual(state[mode][DAY]["status"], "sent")
            self.assertEqual(state[mode][DAY]["recipient_count"], 1)
        self.assertNotIn(RECIPIENTS[0], json.dumps(state))


if __name__ == "__main__":
    unittest.main()
