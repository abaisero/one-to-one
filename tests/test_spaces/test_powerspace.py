import unittest

import more_itertools as mitt

import indextools

from .templates import templates


class PowerBase(unittest.TestCase):
    def setUp(self):
        self.space = self.new_space()

    @staticmethod
    def new_space():
        return indextools.PowerSpace('abc')

    @property
    def values(self):
        return (set(v) for v in mitt.powerset('abc'))


class PowerSpaceTest(PowerBase, templates.SpaceTest):
    def test_nelems(self):
        self.assertEqual(self.space.nelems, 8)


class PowerElemTest(PowerBase, templates.ElemTest):
    pass
