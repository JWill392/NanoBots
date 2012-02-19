#!/usr/bin/python
# -*- coding: utf-8 -*-
# By JWill and BDC, 2011

import CellEntity as CellEntity
import Bot
import unittest


class BotTest(unittest.TestCase):

    def setUp(self):
        self.bot      = Bot.Bot((0, 0), 10)
        self.zero_bot = Bot.Bot((0, 0), 0)
        self.neg_bot  = Bot.Bot((0, 0), -1)

    def test_get_health(self):
        self.assertEqual(10, self.bot.get_health())

    def test_has_health_true(self):
        self.assertTrue(self.bot.has_health())

    def test_has_health_false_on_zero(self):
        self.assertFalse(self.zero_bot.has_health())

    def test_has_health_false_neg_zero(self):
        self.assertFalse(self.neg_bot.has_health())

    def test_sub_health(self):
        self.bot.sub_health(10)
        self.assertEqual(0, self.bot.get_health())
        self.assertFalse(self.bot.has_health())

    def test_sub_health_raise_assert(self):
        self.assertRaises(AssertionError, self.zero_bot.sub_health, 10)

    def test_add_health(self):
        self.bot.add_health(10)
        self.assertEqual(20, self.bot.get_health())
        self.assertTrue(self.bot.has_health())

    #def test_get_inbox(self):
    #    assert False, "TODO"


if __name__ == '__main__':
    unittest.main()
