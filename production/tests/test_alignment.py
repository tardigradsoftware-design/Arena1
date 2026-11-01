import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_alignment import check

class AlignmentTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(check('İlk gün!', [{'word':'ilk', 'start':0.1, 'end':0.4}, {'word':'gün', 'start':0.5, 'end':0.8}], 1), [])
    def test_missing_word(self):
        self.assertTrue(check('İlk gün', [{'word':'ilk','start':0.1,'end':0.4}], 1))
    def test_wrong_word(self):
        self.assertTrue(check('ilk gün', [{'word':'ilk','start':0.1,'end':0.4},{'word':'gece','start':0.5,'end':0.8}], 1))
    def test_overlap_and_out_of_range(self):
        self.assertTrue(check('bir iki', [{'word':'bir','start':0,'end':0.7},{'word':'iki','start':0.6,'end':1.2}], 1))
    def test_missing_timestamp(self):
        self.assertTrue(check('bir', [{'word':'bir','start':0}], 1))

if __name__ == '__main__': unittest.main()
