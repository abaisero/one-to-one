import unittest

import indextools


class SpaceTest(unittest.TestCase):
    def setUp(self):
        self.space = indextools.DomainSpace('abc')
        # TODO find way to  test for multiple types of spaces!
        # all of these tests should pass for any type of space;
        # probably make these tests domain independent..

    def test_space(self):
        space = self.space

        for elem in space.elems:
            with self.subTest(elem=elem):
                self.assertIs(space, elem.space)
                self.assertTrue(space.iselem(elem))

                self.assertEqual(elem.idx, space.idx(elem.value))
                self.assertEqual(elem.value, space.value(elem.idx))

    def test_check_idx(self):
        self.assertRaises(ValueError, self.space._check_idx, -4)
        self.assertEqual(self.space._check_idx(-3), 0)
        self.assertEqual(self.space._check_idx(-2), 1)
        self.assertEqual(self.space._check_idx(-1), 2)
        self.assertEqual(self.space._check_idx(0), 0)
        self.assertEqual(self.space._check_idx(1), 1)
        self.assertEqual(self.space._check_idx(2), 2)
        self.assertRaises(ValueError, self.space._check_idx, 3)

    def test_negative_indices(self):
        self.assertEqual(self.space.value(0), self.space.value(-3))
        self.assertEqual(self.space.value(1), self.space.value(-2))
        self.assertEqual(self.space.value(2), self.space.value(-1))

        for idx in range(self.space.nelems):
            with self.subTest(idx=idx):
                vpos = self.space.value(idx)
                vneg = self.space.value(idx - self.space.nelems)
                self.assertEqual(vpos, vneg)

    def test_elem_idx(self):
        # TODO I don't think this should be a generic test
        e = self.space.elem(0)
        for elem in self.space.elems:
            e.idx = elem.idx
            self.assertEqual(e, elem)

    def test_elem_index(self):
        for e in self.space.elems:
            self.assertEqual(e.__index__(), e.idx)
            self.assertIsInstance(e.__index__(), int)

    def test_elem_equality(self):
        for elem in self.space.elems:
            copy = elem.copy()
            self.assertIsNot(elem, copy)
            self.assertEqual(elem, copy)
            self.assertIs(elem.space, copy.space)

        values = 'abc'
        s1 = indextools.DomainSpace(values)
        s2 = indextools.DomainSpace(values)

        # same value, different space
        self.assertEqual(s1.elem(1), s1.elem(1))
        self.assertNotEqual(s1.elem(1), s2.elem(1))

    def test_space_elem(self):
        space = self.space

        for elem in space.elems:
            with self.subTest(elem=elem):
                self.assertEqual(elem, space.elem(elem.idx))
                self.assertEqual(elem, space.elem(value=elem.value))
                self.assertEqual(elem, space.elem(elem.idx, value=elem.value))

                for idx in range(space.nelems):
                    if idx != elem.idx:
                        with self.subTest(idx=idx):
                            self.assertRaises(ValueError, space.elem, idx=idx,
                                              value=elem.value)

                for value in space.values:
                    if value != elem.value:
                        with self.subTest(value=value):
                            self.assertRaises(ValueError, space.elem,
                                              idx=elem.idx, value=value)

    def test_elem(self):
        values = 'abc'
        s1 = indextools.DomainSpace(values)
        s2 = indextools.DomainSpace(values)

        # same value, different space
        self.assertEqual(s1.elem(1), s1.elem(1))
        self.assertNotEqual(s1.elem(1), s2.elem(1))


# from .spaces import spaces
# for space in spaces:
#     class _SpaceTest(SpaceTest):
#         def setUp(self):
#             self.space = space
