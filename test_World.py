#!/usr/bin/python
# -*- coding: utf-8 -*-
# By JWill and BDC, 2011


import CellEntity
import Bot
import Food
import World
import unittest


class WorldTest(unittest.TestCase):

    def setUp(self):
        self.world = World.World()

    def test_is_game_complete(self):
        self.assertFalse(self.world.is_game_complete())

if __name__ == '__main__':
    unittest.main()
