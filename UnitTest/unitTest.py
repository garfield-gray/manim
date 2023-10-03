import functions as f

import unittest


class testMultiply(unittest.TestCase):
    
    def test_two_positives(self):
        self.assertEqual(f.loopMultiply(10, 15), 10 * 15)

        self.assertEqual(f.loopMultiply(17670, 5415), 17670 * 5415)
    
    def test_one_zeros(self):
        self.assertEqual(f.loopMultiply(0, 15), 0 * 15)

        self.assertEqual(f.loopMultiply(17, 0), 17 * 0)
    
    def test_one_negative(self):
        self.assertEqual(f.loopMultiply(-1, 15), -1 * 15)

        self.assertEqual(f.loopMultiply(17, 0), 17 * 0)
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
