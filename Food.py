#!/usr/bin/python
# -*- coding: utf-8 -*-
# By JWill and BDC, 2011


import CellEntity


class Food(CellEntity.CellEntity):

    def __init__(self, (x, y), energy):
        CellEntity.CellEntity.__init__(self, (x, y))
        self._energy = energy

    def get_energy(self):
        return self._energy

    def has_energy(self):
        return self._energy > 0

    def decrement_energy(self, amount):
        assert self.has_energy(), "No energy - Do not decrement further."
        self._energy -= amount
