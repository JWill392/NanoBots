#!/usr/bin/python
# -*- coding: utf-8 -*-
# By Brody Holden, 2011


import Grid
import unittest


class GridTest(unittest.TestCase):

    def setUp(self):
        self.grid = Grid.Grid(3, 3)

    def test_get_width_square(self):
        self.assertEqual(2, self.grid.get_x())

    def test_get_height_square(self):
        self.assertEqual(2, self.grid.get_y())

    def test_get_width_rect(self):
        rect_grid = Grid.Grid(4, 6)
        self.assertEqual(3, rect_grid.get_x())

    def test_get_height_rect(self):
        rect_grid = Grid.Grid(4, 6)
        self.assertEqual(5, rect_grid.get_y())

    def test_get_grid_square(self):
        self.assertEqual(
            [[None, None, None], [None, None, None], [None, None, None]],
            self.grid.get_grid(),
        )

    def test_get_grid_x2_by_y3(self):
        g = Grid.Grid(2, 3)
        self.assertEqual(
            [[None, None], [None, None], [None, None]],
            g.get_grid(),
        )

    def test_get_grid_x3q_by_y2(self):
        g = Grid.Grid(3, 2)
        self.assertEqual(
            [[None, None, None], [None, None, None]],
            g.get_grid(),
        )

    def test_set_cell(self):
        self.grid.set_cell(1, 2, "TEST")
        self.assertEqual(
            [[None, None, None], [None, None, None], [None, "TEST", None]],
            self.grid.get_grid(),
        )

    def test_set_cell_two(self):
        self.grid.set_cell(1, 2, "FIRST")
        self.grid.set_cell(2, 2, "SECOND")
        self.assertEqual(
            [
                [None, None, None],
                [None, None, None],
                [None, "FIRST", "SECOND"],
            ],
            self.grid.get_grid(),
        )

    def test_set_cell_none(self):
        self.grid.set_cell(1, 2, "TEST")
        self.assertEqual(
            [[None, None, None], [None, None, None], [None, "TEST", None]],
            self.grid.get_grid(),
        )
        self.grid.set_cell(1, 2, None)
        self.assertEqual(
            [[None, None, None], [None, None, None], [None, None, None]],
            self.grid.get_grid(),
        )

    def test_get_cell(self):
        self.grid.set_cell(1, 2, "TEST")
        self.assertEqual("TEST", self.grid.get_cell(1, 2))

    def test_get_cell_none(self):
        self.assertEqual(None, self.grid.get_cell(1, 2,))

    def test_get_cell_wall_both_under(self):
        self.assertEqual("WALL", self.grid.get_cell(-1, -1))

    def test_get_cell_wall_both_x_under(self):
        self.assertEqual("WALL", self.grid.get_cell(-1, 1))

    def test_get_cell_wall_both_y_under(self):
        self.assertEqual("WALL", self.grid.get_cell(1, -1))

    def test_get_cell_wall_both_over(self):
        self.assertEqual("WALL", self.grid.get_cell(3, 3,))

    def test_get_cell_wall_x_over(self):
        self.assertEqual("WALL", self.grid.get_cell(3, 1,))

    def test_get_cell_wall_y_over(self):
        self.assertEqual("WALL", self.grid.get_cell(1, 3,))

    def test_get_neighborhood_center(self):
        self.grid.set_cell(0, 0, "0,0")
        self.grid.set_cell(1, 0, "1,0")
        self.grid.set_cell(2, 0, "2,0")
        self.grid.set_cell(0, 1, "0,1")
        self.grid.set_cell(1, 1, "1,1")
        self.grid.set_cell(2, 1, "2,1")
        self.grid.set_cell(0, 2, "0,2")
        self.grid.set_cell(1, 2, "1,2")
        self.grid.set_cell(2, 2, "2,2")
        self.assertEqual(
            [
                ["0,0", "1,0", "2,0"],
                ["0,1", "1,1", "2,1"],
                ["0,2", "1,2", "2,2"],
            ],
            self.grid.get_neighborhood(1, 1, 1),
        )

    def test_get_neighborhood_21(self):
        self.grid.set_cell(0, 0, "0,0")
        self.grid.set_cell(1, 0, "1,0")
        self.grid.set_cell(2, 0, "2,0")
        self.grid.set_cell(0, 1, "0,1")
        self.grid.set_cell(1, 1, "1,1")
        self.grid.set_cell(2, 1, "2,1")
        self.grid.set_cell(0, 2, "0,2")
        self.grid.set_cell(1, 2, "1,2")
        self.grid.set_cell(2, 2, "2,2")
        self.assertEqual(
            [
                ["1,0", "2,0", "WALL"],
                ["1,1", "2,1", "WALL"],
                ["1,2", "2,2", "WALL"],
            ],
            self.grid.get_neighborhood(2, 1, 1),
        )
        # grid
        # [
        #   ["0,0", "1,0", "2,0"],
        #   ["0,1", "1,1", "2,1"],
        #   ["0,2", "1,2", "2,2"]
        # ]
        # "2,1"'s neighborhood
        # [
        #   ["1,0", "2,0", "WALL"],
        #   ["1,1", "2,1", "WALL"],
        #   ["1,2", "2,2", "WALL"]
        # ]

    def test_get_neighborhood_center_radius_2(self):
        self.grid.set_cell(0, 0, "0,0")
        self.grid.set_cell(1, 0, "1,0")
        self.grid.set_cell(2, 0, "2,0")
        self.grid.set_cell(0, 1, "0,1")
        self.grid.set_cell(1, 1, "1,1")
        self.grid.set_cell(2, 1, "2,1")
        self.grid.set_cell(0, 2, "0,2")
        self.grid.set_cell(1, 2, "1,2")
        self.grid.set_cell(2, 2, "2,2")
        self.assertEqual(
            [
                ["WALL", "WALL", "WALL", "WALL", "WALL"],
                ["WALL", "0,0",  "1,0",  "2,0",  "WALL"],
                ["WALL", "0,1",  "1,1",  "2,1",  "WALL"],
                ["WALL", "0,2",  "1,2",  "2,2",  "WALL"],
                ["WALL", "WALL", "WALL", "WALL", "WALL"],
            ],
            self.grid.get_neighborhood(1, 1, 2),
        )


if __name__ == '__main__':
    unittest.main()
