import unittest

import indextools


class DomainSpaceTest(unittest.TestCase):
    def setUp(self):
        self.space = indextools.DomainSpace('abc')

    def test_domain_init(self):
        self.assertEqual(self.space.nelems, 3)

    def test_domain_init_error(self):
        self.assertRaises(ValueError, indextools.DomainSpace, 'aab')

    def test_domain_idx(self):
        self.assertEqual(self.space.idx('a'), 0)
        self.assertEqual(self.space.idx('b'), 1)
        self.assertEqual(self.space.idx('c'), 2)

    def test_domain_value(self):
        self.assertEqual(self.space.value(0), 'a')
        self.assertEqual(self.space.value(1), 'b')
        self.assertEqual(self.space.value(2), 'c')

    def test_domain_values(self):
        self.assertCountEqual(self.space.values, 'abc')


class BoolSpaceTest(unittest.TestCase):
    def setUp(self):
        self.space = indextools.BoolSpace()

    def test_bool_init(self):
        self.assertEqual(self.space.nelems, 2)

    def test_bool_value(self):
        self.assertEqual(self.space.value(False), 0)
        self.assertEqual(self.space.value(True), 1)

    def test_bool_idx(self):
        self.assertEqual(self.space.idx(False), 0)
        self.assertEqual(self.space.idx(True), 1)

    def test_bool_values(self):
        self.assertCountEqual(self.space.values, (False, True))


class RangeSpaceTest(unittest.TestCase):
    def test_range_init_error(self):
        # checks that same errors as `range` are thrown
        self.assertRaises(TypeError, indextools.RangeSpace)
        self.assertRaises(ValueError, indextools.RangeSpace, 0, 0, 0)
        self.assertRaises(TypeError, indextools.RangeSpace, 0, 0, 0, 0)

    def test_range_stop(self):
        space = indextools.RangeSpace(10)

        self.assertEqual(space.nelems, 10)
        self.assertCountEqual(space.values, range(10))

    def test_range_start(self):
        space = indextools.RangeSpace(-6, 10)

        self.assertEqual(space.nelems, 16)
        self.assertCountEqual(space.values, range(-6, 10))

    def test_range_step(self):
        space = indextools.RangeSpace(-6, 10, 2)

        self.assertEqual(space.nelems, 8)
        self.assertCountEqual(space.values, range(-6, 10, 2))
