_novalue = object()


class Elem:
    def __init__(self, space, idx):
        """Element of an indexing space.

        :param space: A Space, an indexing space.
        :param idx: An int, an index in the space.
        """
        self.space = space
        self.idx = idx

    def __index__(self):
        # NOTE has to be very specific type (e.g. np.int64 not allowed)
        return int(self.idx)

    @property
    def value(self):
        """Return element value."""
        return self.space.value(self.idx)

    @value.setter
    def value(self, value):
        """Set element value."""
        self.idx = self.space.idx(value)

    def copy(self):
        """Return copy of self from same indexing space."""
        return self.space.elem(self.idx)

    def __eq__(self, other):
        """Check equality against other element or value."""
        try:
            return self.space is other.space and self.idx == other.idx
        except AttributeError:
            return self.value == other

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.space) ^ hash(self.idx)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'Elem({self.idx}: {self.value})'


class Space:
    Elem = Elem

    def value(self, idx):
        """Return value in this indexing space corresponding to ``idx``."""
        raise NotImplementedError

    def idx(self, value):
        """Return index in this indexing space corresponding to ``value``."""
        raise NotImplementedError

    def elem(self, idx=None, *, value=_novalue):
        """Return element of this indexing space.

        Usage::

            >>> import indextools
            >>> space = indextools.DomainSpace(('red', 'green', 'blue'))
            >>> elem = space.elem(1)
            >>> elem = space.elem(value='red')

        :param idx: The index of the element.
        :param value: The value of the element.
        :rtype: A :class:`Elem <Elem>`
        """
        if idx is not None and value is not _novalue \
                and self.value(idx) != value:
            raise ValueError(f'Index ({idx}) and value ({value}) do not match')
        if idx is None:
            idx = self.idx(value)

        return self.Elem(self, idx)  # NOTE this might be annoying for union...

    def isvalue(self, value):
        """ Check whether ``value`` belongs to this indexing space."""
        try:
            self.idx(value)
        except ValueError:
            return False
        return True

    def iselem(self, elem):
        """Check whether ``elem`` belongs to this indexing space."""
        try:
            return elem.space is self and 0 <= elem.idx < self.nelems
        except AttributeError:
            return False

    @property
    def values(self):
        """Return generator over values of indexing space."""
        return map(self.value, range(self.nelems))

    @property
    def elems(self):
        """Return generator of elements in indexing space."""
        return map(self.elem, range(self.nelems))

    def items(self):
        """Return generator of index-value pairs in indexing space."""
        for idx in range(self.nelems):
            yield idx, self.value(idx)

    def _check_idx(self, idx):
        """Check index within range, and returns non-negative equivalent."""
        if not -self.nelems <= idx < self.nelems:
            raise ValueError(f'Invalid index ({idx}) is outside of range '
                             f'[0, {self.nelems}).')
        return idx % self.nelems

    def __contains__(self, other):
        """Check whether `other` is element or value of this space."""
        return self.iselem(other) or self.isvalue(other)

    def __len__(self):
        """Return number of elements in this space."""
        return self.nelems
