import unittest

import indextools


class UnionSpaceTest(unittest.TestCase):
    def setUp(self):
        self.space = indextools.UnionSpace(
            indextools.BoolSpace(),
            indextools.DomainSpace('abc'),
            indextools.RangeSpace(10, 20, 2),
        )

    def test_union_init(self):
        self.assertEqual(self.space.nelems, 10)

    def test_union_init_error(self):
        self.assertRaises(ValueError, indextools.UnionSpace,
                indextools.BoolSpace(), indextools.BoolSpace())

    def test_union_value(self):
        self.assertEqual(self.space.value(0), False)
        self.assertEqual(self.space.value(1), True)
        self.assertEqual(self.space.value(2), 'a')
        self.assertEqual(self.space.value(3), 'b')
        self.assertEqual(self.space.value(4), 'c')
        self.assertEqual(self.space.value(5), 10)
        self.assertEqual(self.space.value(6), 12)
        self.assertEqual(self.space.value(7), 14)
        self.assertEqual(self.space.value(8), 16)
        self.assertEqual(self.space.value(9), 18)

    def test_union_idx(self):
        self.assertEqual(self.space.idx(False), 0)
        self.assertEqual(self.space.idx(True), 1)
        self.assertEqual(self.space.idx('a'), 2)
        self.assertEqual(self.space.idx('b'), 3)
        self.assertEqual(self.space.idx('c'), 4)
        self.assertEqual(self.space.idx(10), 5)
        self.assertEqual(self.space.idx(12), 6)
        self.assertEqual(self.space.idx(14), 7)
        self.assertEqual(self.space.idx(16), 8)
        self.assertEqual(self.space.idx(18), 9)
