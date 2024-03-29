import unittest

import one_to_one

from .templates import templates


class BoolBase:
    @staticmethod
    def new_space():
        return one_to_one.BoolSpace()

    @property
    def values(self):
        return (False, True)


class BoolSpaceTest(BoolBase, templates.SpaceTest):
    def test_nelems(self):
        self.assertEqual(self.space.nelems, 2)


class BoolElemTest(BoolBase, templates.ElemTest):
    pass
