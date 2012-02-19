#!/usr/bin/python
# -*- coding: utf-8 -*-
# By JWill and BDC, 2011


class CellEntity:
    """A cell entity has a x and y position."""

    def __init__(self, (x, y)):
        """Initally set x and y position."""
        self._x = x
        self._y = y

    def get_pos(self):
        """Get tuple of x and y position."""
        return (self._x, self._y)

    def set_pos(self, (x, y)):
        """Set x and y position."""
        self._x = x
        self._y = y
