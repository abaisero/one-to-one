import unittest

import indextools


class PowerSpaceTest(unittest.TestCase):
    def setUp(self):
        self.space = indextools.PowerSpace('abc')

    def test_power_init(self):
        self.assertEqual(self.space.nelems, 8)

    def test_power_value(self):
        self.assertEqual(self.space.value(0), set())
        self.assertEqual(self.space.value(7), set('abc'))

    def test_power_idx(self):
        self.assertEqual(self.space.idx(set()), 0)
        self.assertEqual(self.space.idx(set('abc')), 7)
