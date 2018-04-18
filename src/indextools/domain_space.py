from .space import Space


class DomainSpace(Space):
    def __init__(self, domain):
        """Domain-based indexing space.

        :param iterable: An iterable, the domain.
        """
        super().__init__()
        if len(set(domain)) != len(domain):
            raise ValueError('Domain should not have values which are equal.')

        self.domain = tuple(domain)
        self.nelems = len(self.domain)
        self._indices = {value: idx for idx, value in enumerate(self.domain)}

    def value(self, idx):
        return self.domain[idx]

    def idx(self, value):
        """Return index corresponding to ``value``."""
        try:
            return self._indices[value]
        except KeyError:
            raise ValueError(f'Invalid value ({value}) does not belong to '
                             'this domain space.')


class BoolSpace(DomainSpace):
    def __init__(self):
        """Alias for DomainSpace((False, True))."""
        super().__init__((False, True))


# Less efficient
# class RangeSpace(DomainSpace):
#     def __init__(self, *args):
#         """Alias for DomainSpace(range(*args))."""
#         super().__init__(range(*args))


class RangeSpace(Space):
    """More efficient than DomainSpace(range(*args))."""

    def __init__(self, *args):
        super().__init__()
        self.domain = range(*args)
        self.nelems = len(self.domain)

    def value(self, idx):
        return self.domain[idx]

    def idx(self, value):
        return self.domain.index(value)
