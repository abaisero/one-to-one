from .space import Space


class PowerElem(Space.Elem):
    def update(self, *, include, exclude):
        include = set(include)
        exclude = set(exclude)
        self.value = (self.value - exclude) | (include - exclude)

    def include(self, value):
        self.value |= value

    def exclude(self, value):
        self.value -= value


class PowerSpace(Space):
    Elem = PowerElem

    def __init__(self, values):
        """Powerset space.

        :param values: An iterable, the values of the powerset space.
        """
        super().__init__()

        self._vlist = tuple(values)
        self._vbits = {value: 1 << bit for bit, value in enumerate(self._vlist)}
        self._nbits = len(self._vlist)
        self.nelems = 1 << self._nbits

    def value(self, idx):
        idx = self._check_idx(idx)
        bits = (k for k in range(self._nbits) if idx >> k & 1)
        return set(self._vlist[bit] for bit in bits)

    def idx(self, value):
        return sum(self._vbits[v] for v in value)
