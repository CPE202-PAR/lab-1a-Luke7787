# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *


class TestLocation(unittest.TestCase):

    def test_repr(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

    def test_repr_2(self) -> None:
        loc = Location("Canada", 0.0, 0.0)
        self.assertEqual(repr(loc),"Location('Canada', 0.0, 0.0)")


if __name__ == "__main__":
    unittest.main()
