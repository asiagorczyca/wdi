import unittest
import pytest
from zad5_lab9_class import Complexnum

# część na testy w unittest
class TestComplexnum(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Complexnum(1, 1).add(Complexnum(1, 1)), Complexnum(2, 2))
        self.assertEqual(Complexnum(1, 1).add(Complexnum(-1, -1)), Complexnum(0, 0))
        self.assertEqual(Complexnum(1, 1).add(Complexnum(0, 0)), Complexnum(1, 1))
        self.assertEqual(Complexnum(1, 1).add(Complexnum(0, 1)), Complexnum(1, 2))

    def test_subtract(self):
        self.assertEqual(Complexnum(1, 1).subtract(Complexnum(1, 1)), Complexnum(0, 0))
        self.assertEqual(Complexnum(1, 1).subtract(Complexnum(-1, -1)), Complexnum(2, 2))
        self.assertEqual(Complexnum(1, 1).subtract(Complexnum(0, 0)), Complexnum(1, 1))
        self.assertEqual(Complexnum(1, 1).subtract(Complexnum(0, 1)), Complexnum(1, 0))

    def test_multiply(self):
        self.assertEqual(Complexnum(1, 1).multiply(Complexnum(1, 1)), Complexnum(0, 2))
        self.assertEqual(Complexnum(1, 1).multiply(Complexnum(-1, -1)), Complexnum(0, -2))
        self.assertEqual(Complexnum(1, 1).multiply(Complexnum(0, 0)), Complexnum(0, 0))
        self.assertEqual(Complexnum(1, 1).multiply(Complexnum(0, 1)), Complexnum(-1, 1))


unittest.main(argv=[''], verbosity=2, exit=False)

# część na testy w pytest

def test_divide():
    assert Complexnum(1, 1).divide(Complexnum(1, 1)) == Complexnum(1, 0)
    assert Complexnum(1, 1).divide(Complexnum(-1, -1)) == Complexnum(-1, 0)
    assert Complexnum(1, 1).divide(Complexnum(0, 1)) == Complexnum(1, -1)

def test_exp():
    assert Complexnum(1, 1).exp(0) == 1
    assert Complexnum(1, 1).exp(1) == Complexnum(1, 1)
    assert Complexnum(1, 1).exp(2) == Complexnum(0, 2)
    assert Complexnum(1, 1).exp(3) == Complexnum(-2, 2)

def test_find_root():
    assert Complexnum(-25, 0).find_root() == Complexnum(0, 5)
    assert Complexnum(6, -8).find_root() == Complexnum(2*(2**(1/2)), -2**(1/2))
    assert Complexnum(0, 2).find_root() == Complexnum(1, 1)

