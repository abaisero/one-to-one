import unittest

import indextools


class PalindromeTest(unittest.TestCase):
    @staticmethod
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    def test_palindromes(self):
        integers = indextools.RangeSpace(200)
        palindromes = indextools.SubSpace(integers, self.is_palindrome)

        palindromes_real = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191

        self.assertEqual(palindromes.nelems, len(palindromes_real))
        for i, palindrome_ith in enumerate(palindromes_real):
            self.assertEqual(palindromes.value(i), palindrome_ith)


