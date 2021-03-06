# CPE 202 Lab 1 Test Cases

import unittest
from lab1a import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_01(self) -> None:
        tlist = [1,2,3]
        self.assertEqual(max_list_iter(tlist),3)

    def test_max_list_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_03(self):
        t_list = []
        self.assertEqual(max_list_iter(t_list), None)

    def test_reverse_NoneTest(self):
        t_list = None
        with self.assertRaises(ValueError):
            reverse_list(None)

    def test_reverse(self) -> None:
        intlist = [1,2,3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist,[3,2,1])
        self.assertEqual(intlist,[1,2,3])

    def test_reverse_mutate(self) -> None:
        intlist = [1,2,3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist,[3,2,1])
        self.assertEqual(intlist,[1,2,3])

if __name__ == "__main__":
        unittest.main()
