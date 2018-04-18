import unittest

import indextools


class FactoryFilterTest(unittest.TestCase):
    @staticmethod
    def is_prime(n):
        return n > 1 and all(n % i != 0 for i in range(2, n))

    @staticmethod
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    def test_factory(self):
        integers = indextools.RangeSpace(100)

        palindromes = indextools.SubSpace(integers, self.is_palindrome)
        self.assertEqual(palindromes.nelems, 19)
        for i in palindromes.values:
            self.assertTrue(self.is_palindrome(i))

        primes = indextools.SubSpace(integers, self.is_prime)
        self.assertEqual(primes.nelems, 25)
        for i in primes.values:
            self.assertTrue(self.is_prime(i))
