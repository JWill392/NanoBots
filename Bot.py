#!/usr/bin/python
# -*- coding: utf-8 -*-
# By JWill and BDC, 2011


import CellEntity


class Bot(CellEntity.CellEntity):

    def __init__(self, (x, y), health):
        CellEntity.CellEntity.__init__(self, (x, y))
        self._health = health

    def get_health(self):
        return self._health

    def has_health(self):
        return self._health > 0

    def sub_health(self, amount):
        assert self.has_health(), "No health - Do not decrement further."
        self._health -= amount

    def add_health(self, amount):
        self._health += amount

    #def get_inbox(self):
    #    assert False, "TODO."
