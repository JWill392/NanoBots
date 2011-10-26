#!/usr/bin/python
# -*- coding: utf-8 -*-
# By Jackson Williams and Brody Holden, 2011


import CellEntity
import Food
import unittest


class FoodTest(unittest.TestCase):

    def setUp(self):
        self.food      = Food.Food((0, 0), 10)
        self.zero_food = Food.Food((0, 0), 0)

    def test_get_energy(self):
        self.assertEqual(10, self.food.get_energy())

    def test_has_energy_true(self):
        self.assertTrue(self.food.has_energy())

    def test_has_energy_false_on_zero(self):
        self.assertFalse(self.zero_food.has_energy())

    def test_has_energy_false_below_zero(self):
        below_food = Food.Food((0, 0), -1)
        self.assertFalse(below_food.has_energy())

    def test_decrement_energy(self):
        self.food.decrement_energy(10)
        self.assertEqual(0, self.food.get_energy())
        self.assertFalse(self.food.has_energy())

    def test_decrement_energy_raise_assert(self):
        self.assertRaises(AssertionError, self.zero_food.decrement_energy, 10)


if __name__ == '__main__':
    unittest.main()
