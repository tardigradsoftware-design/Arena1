import sys
import unittest
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audio_audit import analyze

class AudioAuditTests(unittest.TestCase):
    def test_quiet_span(self):
        s = np.concatenate([np.full(8000, .1), np.zeros(8000), np.full(8000, .1)])
        r = analyze(s)
        self.assertEqual(r['seconds_analyzed'], 1.5)
        self.assertEqual(r['quiet_intervals_below_minus_45dbfs'], [{'start': .5, 'end': 1.0}])
    def test_clipping(self):
        self.assertEqual(analyze(np.ones(1000))['near_full_scale_percent'], 100)
    def test_empty(self):
        with self.assertRaises(ValueError): analyze([])

if __name__ == '__main__': unittest.main()
