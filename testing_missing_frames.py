import unittest
from missing_frames import find_missing_ranges

class TestMissingFrames(unittest.TestCase):
    def test_example(self):
        frames = [1, 2, 3, 5, 6, 10, 11, 16]
        expected = {
            "gaps": [[4, 4], [7, 9], [12, 15]],
            "longest_gap": [12, 15],
            "missing_count": 8
        }
        self.assertEqual(find_missing_ranges(frames), expected)

    def test_empty(self):
        self.assertEqual(find_missing_ranges([]),
                         {"gaps": [], "longest_gap": [], "missing_count": 0})

    def test_start_gap(self):
        self.assertEqual(find_missing_ranges([3, 4, 5]),
                         {"gaps": [[1, 2]], "longest_gap": [1, 2], "missing_count": 2})

    def test_single(self):
        self.assertEqual(find_missing_ranges([1]),
                         {"gaps": [], "longest_gap": [], "missing_count": 0})

if __name__ == "__main__":
    unittest.main()
