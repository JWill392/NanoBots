#!/usr/bin/python
# -*- coding: utf-8 -*-
# By JWill and BDC, 2011


import copy


class Grid:
    """ Grid
        - Indexed from zero.
        - Pass values as x, y.
        - Interally it's y, x.

    To the outside, a 3 by 3 grid is:
    -------------------
    | x,y | x,y | x,y |
    -------------------------
    | 0,0 | 1,0 | 2,0 | x,y |
    -------------------------
    | 0,1 | 1,1 | 2,1 | x,y |
    -------------------------
    | 0,2 | 1,2 | 2,2 | x,y |
    -------------------------
    """

    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._grid = []

        for i in range(height):
            self._grid.append([])
            for j in range(width):
                self._grid[i].append(None)

    def _is_in_bounds(self, x, y):
        if (x < 0 or x >= self._x or
            y < 0 or y >= self._y):
            return False

        return True

    def get_x(self):
        return self._x - 1

    def get_y(self):
        return self._y - 1

    def get_cell(self, x, y):
        if not self._is_in_bounds(x, y):
            return "WALL"       #- Magic string

        return self._grid[y][x] # Note: y, x

    def set_cell(self, x, y, ref):
        self._grid[y][x] = ref

    def get_grid(self):
        return copy.deepcopy(self._grid)

    def get_neighborhood(self, x, y, radius):
        """
        radius = 1 -> 3 x 3 list -> size = (r * 2) + 1 = 3
        radius = 2 -> 5 x 5 list -> size = (r * 2) + 1 = 5
        """
        hood = []
        size = (radius * 2) + 1

        for i in range(0 - radius, size - radius):
            t = []

            for j in range(0 - radius, size - radius):
                t.append(
                    self.get_cell(x + j, y + i),
                )

            hood.append(t)

        return hood
