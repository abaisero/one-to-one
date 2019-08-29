import numpy as np

from .space import Space

# class SubElem(Space.Elem):
#     def __init__(self, space, idx):
#         self.space = space
#         self.idx = idx

#     @property
#     def idx(self):
#         sidx = self.selem.idx
#         return self.space.sidx_to_idx(sidx)

#     @idx.setter
#     def idx(self, idx):
#         try:
#             self.selem.sidx = self.space.idx_to_sidx(idx)
#         except AttributeError:
#             self.selem = self.space.selem(idx)

#     @idx.setter
#     def idx(self, idx):
#         try:
#             self.selem.sidx = self.space.idx_to_sidx(idx)
#         except AttributeError:
#             self.selem = self.space.selem(idx)

#     def __getattr__(self, name):
#         try:
#             return getattr(super().__dict__['felem'], name)
#         except KeyError:
#             raise AttributeError


class SubSpace(Space):
    def __init__(self, space, *filters):
        """Subspace, containing only filtered elements.

        :param space: A Space.
        :param *filters: Filters.
        """
        super().__init__()

        self.space = space
        self.filters = filters

        _if = np.array(
            [[idx, self.filter(value)] for idx, value in space.items()]
        )
        _f = _if[:, 1].astype(bool)

        self._valid_indices = _if[_f, 0]
        self._num_nonvalids_before = np.cumsum(~_f)
        self.nelems = space.nelems - self._num_nonvalids_before[-1]

    def filter(self, value):
        if not self.space.isvalue(value):
            raise ValueError(
                f'Invalid value ({value}) does not belong to space'
            )

        return all(f(value) for f in self.filters)

    def value(self, idx):
        idx = self._check_idx(idx)
        sidx = self._idx_to_sidx(idx)
        return self.space.value(sidx)

    def idx(self, value):
        if not self.filter(value):
            raise ValueError(f'Invalid value ({value}) does not satisfy filter')
        sidx = self.space.idx(value)
        return self._sidx_to_idx(sidx)

    def _idx_to_sidx(self, idx):
        return self._valid_indices[idx]

    def _sidx_to_idx(self, sidx):
        return sidx - self._num_nonvalids_before[sidx]

    def supidx(self, idx):
        """Return SuperSet index corresponding to the SubSpace's index."""
        idx = self._check_idx(idx)
        return self._idx_to_sidx(idx)

    # TODO maybe only provide supidx
    def supelem(self, idx):
        """Return SuperSet element corresponding to the SubSpace's index."""
        sidx = self.supidx(idx)
        return self.space.elem(sidx)
