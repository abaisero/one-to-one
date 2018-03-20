import unittest
import types

import indextools


class JointSpaceTest(unittest.TestCase):
    def setUp(self):
        self.s0 = indextools.BoolSpace()
        self.s1 = indextools.DomainSpace('abc')
        self.s2 = indextools.RangeSpace(4)
        self.space = indextools.JointSpace(
            self.s0,
            self.s1,
            self.s2,
        )

    def test_joint_init(self):
        self.assertEqual(self.space.nelems, 24)

    def test_joint_getitem(self):
        self.assertIs(self.space[-3], self.s0)
        self.assertIs(self.space[-2], self.s1)
        self.assertIs(self.space[-1], self.s2)
        self.assertIs(self.space[0], self.s0)
        self.assertIs(self.space[1], self.s1)
        self.assertIs(self.space[2], self.s2)

    def test_joint_getitem_error(self):
        self.assertRaises(IndexError, self.space.__getitem__, -4)
        self.assertRaises(IndexError, self.space.__getitem__, 3)

    def test_joint_value(self):
        self.assertEqual(self.space.value(0), (False, 'a', 0))
        self.assertEqual(self.space.value(23), (True, 'c', 3))

    def test_joint_idx(self):
        self.assertEqual(self.space.idx((False, 'a', 0)), 0)
        self.assertEqual(self.space.idx((True, 'c', 3)), 23)


class JointNamedSpaceTest(unittest.TestCase):
    def setUp(self):
        self.s0 = indextools.BoolSpace()
        self.s1 = indextools.DomainSpace('abc')
        self.s2 = indextools.RangeSpace(4)
        self.space = indextools.JointNamedSpace(
            s0=self.s0,
            s1=self.s1,
            s2=self.s2,
        )

    def test_jointnamed_init(self):
        self.assertEqual(self.space.nelems, 24)

    def test_jointnamed_getattr(self):
        self.assertIs(self.space.s0, self.s0)
        self.assertIs(self.space.s1, self.s1)
        self.assertIs(self.space.s2, self.s2)

    def test_jointnamed_getattr_error(self):
        self.assertRaises(AttributeError, self.space.__getattr__, 's_')
        self.assertRaises(AttributeError, self.space.__getattr__, 's3')

    def test_jointnamed_value(self):
        value = self.space.value(0)
        self.assertEqual(value.s0, False)
        self.assertEqual(value.s1, 'a')
        self.assertEqual(value.s2, 0)

        value = self.space.value(23)
        self.assertEqual(value.s0, True)
        self.assertEqual(value.s1, 'c')
        self.assertEqual(value.s2, 3)

    def test_jointnamed_idx(self):
        value = types.SimpleNamespace(s0=False, s1='a', s2=0)
        self.assertEqual(self.space.idx(value), 0)

        value = types.SimpleNamespace(s0=True, s1='c', s2=3)
        self.assertEqual(self.space.idx(value), 23)
