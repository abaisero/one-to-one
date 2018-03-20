import unittest

import indextools


class PrimeTest(unittest.TestCase):
    @staticmethod
    def is_prime(n):
        return n>1 and all(n%i!=0 for i in range(2, n))

    def test_primes(self):
        integers = indextools.RangeSpace(200)
        primes = indextools.SubSpace(integers, self.is_prime)

        primes_real = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199

        self.assertEqual(primes.nelems, len(primes_real))
        for i, prime_ith in enumerate(primes_real):
            self.assertEqual(primes.value(i), prime_ith)
