from .space import Space

# from collections import namedtuple
import types
import numpy as np


class _JointSpace_Base:
    def _ravel_multi_index(self, indices):
        return int(np.ravel_multi_index(indices, self._dims))

    def _unravel_index(self, idx):
        return np.unravel_index(idx, self._dims)


class JointElem(Space.Elem):
    @property
    def idx(self):
        indices = tuple(s.idx for s in self.elems.values())
        return self.space._ravel_multi_index(indices)

    @idx.setter
    def idx(self, idx):
        try:
            elems = self.elems.values()
        except AttributeError:
            self.elems = self.space._etuple(idx)
        else:
            indices = self.space._unravel_index(idx)
            for eidx, elem in zip(indices, elems):
                elem.idx = eidx

    def __getitem__(self, key):
        return self.elems[key]

    # TODO when setting smth which is a subitem;  actually set a value!!
    # TODO to avoid item.p = value (instead of item.p.value = ...) bug
    # def __setattribute__(self, name, value):
    #     # TODO if
    #     if name in super().__dict__['imap']:
    #         getattr(self, name).value = value
    #     else:
    #     try:
    #         super().__dict__['imap'][name]
    #     except KeyError


class JointSpace(Space, _JointSpace_Base):
    Elem = JointElem

    def __init__(self, *spaces):
        """Product space of input spaces, themselves accessed via index.

        :param *spaces: Spaces.
        """
        self.spaces = spaces
        self._dims = tuple(s.nelems for s in spaces)
        self.nelems = np.prod(self._dims)

    def __getitem__(self, key):
        return self.spaces[key]

    def idx(self, value):
        indices = tuple(s.idx(v) for s, v in zip(self.spaces, value))
        return self._ravel_multi_index(indices)

    def value(self, idx):
        idx = self._check_idx(idx)
        indices = self._unravel_index(idx)
        return tuple(s.value(sidx) for s, sidx in zip(self.spaces, indices))

    def _etuple(self, idx):
        idx = self._check_idx(idx)
        indices = self._unravel_index(idx)
        return tuple(s.elem(sidx) for s, sidx in zip(self.spaces, indices))


class JointNamedElem(Space.Elem):
    """JointNamedSpace.Elem does not contain an explicit index;  Rather, it uses the indices of the chilren elems!"""

    @property
    def idx(self):
        indices = tuple(e.idx for e in self.elems.values())
        return self.space._ravel_multi_index(indices)

    @idx.setter
    def idx(self, idx):
        try:
            elems = self.elems.values()
        except AttributeError:
            self.elems = self.space._edict(idx)
        else:
            indices = self.space._unravel_index(idx)
            for eidx, elem in zip(indices, elems):
                elem.idx = eidx

    def __getattr__(self, attr):
        try:
            return super().__dict__['elems'][attr]
        except KeyError:
            raise AttributeError

    # TODO when setting smth which is a subitem;  actually set a value!!
    # TODO to avoid item.p = value (instead of item.p.value = ...) bug
    # def __setattribute__(self, name, value):
    #     # TODO if
    #     if name in super().__dict__['imap']:
    #         getattr(self, name).value = value
    #     else:
    #     try:
    #         super().__dict__['imap'][name]
    #     except KeyError


class JointNamedSpace(Space, _JointSpace_Base):
    Elem = JointNamedElem

    def __init__(self, **spaces):
        """Product space of named input spaces, themselves accessed via attribute.

        :param **spaces: Named spaces.
        """
        self.spaces = spaces
        self._dims = tuple(s.nelems for s in spaces.values())
        self.nelems = np.prod(self._dims)
        # self.JointNamedValue = namedtuple('JointNamedValue', spaces.keys())

    def __getattr__(self, attr):
        try:
            return self.spaces[attr]
        except KeyError:
            raise AttributeError

    def value(self, idx):
        indices = self._unravel_index(idx)
        return types.SimpleNamespace(**{name: s.value(sidx)
            for (name, s), sidx in zip(self.spaces.items(), indices)
        })
        # return self.JointNamedValue(**{name: s.value(sidx)
        #     for (name, s), sidx in zip(self.spaces.items(), indices)
        # })

    def idx(self, value):
        indices = tuple(s.idx(getattr(value, name))
            for name, s in self.spaces.items()
        )
        return self._ravel_multi_index(indices)

    def _edict(self, idx):
        indices = self._unravel_index(idx)
        return {name: s.elem(sidx)
            for (name, s), sidx in zip(self.spaces.items(), indices)
        }
