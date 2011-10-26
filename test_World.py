#!/usr/bin/python
# -*- coding: utf-8 -*-
# By Jackson Williams and Brody Holden, 2011


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
