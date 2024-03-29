import unittest

import one_to_one


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


class PalindromeTest(unittest.TestCase):
    def test_palindromes(self):
        int_space = one_to_one.RangeSpace(100, 200)
        palindrome_space = one_to_one.SubSpace(int_space, is_palindrome)
        values = (101, 111, 121, 131, 141, 151, 161, 171, 181, 191)

        self.assertEqual(palindrome_space.nelems, len(values))
        self.assertCountEqual(palindrome_space.values, values)
