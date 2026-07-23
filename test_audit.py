import unittest
from audit import audit
class TestAudit(unittest.TestCase):
    def test_ready(self):
        x={"action_id":"a","meeting_date":"2026-01-01","owner":"N","source_segment_id":"s","confidence":.9,"auto_dispatch":True}
        self.assertEqual(audit([x])["review_count"],0)
    def test_blocks_low_confidence_dispatch(self):
        x={"action_id":"a","meeting_date":"2026-01-01","owner":"N","source_segment_id":"s","confidence":.2,"auto_dispatch":True}
        self.assertIn("low_confidence_dispatch",audit([x])["actions"][0]["codes"])
if __name__=="__main__": unittest.main()
