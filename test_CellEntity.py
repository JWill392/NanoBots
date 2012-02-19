#!/usr/bin/python
# -*- coding: utf-8 -*-
# By JWill and BDC, 2011


import CellEntity
import unittest


class CellEntityTest(unittest.TestCase):

    def setUp(self):
        self.cell = CellEntity.CellEntity((0, 0))

    def test_get_pos(self):
        self.assertEqual((0, 0), self.cell.get_pos())

    def test_set_pos(self):
        self.cell.set_pos((1, 1))
        self.assertEqual((1, 1), self.cell.get_pos())


if __name__ == '__main__':
    unittest.main()
