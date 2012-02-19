#! /usr/bin/python
# -*- coding: utf-8 -*-
# By JWill and BDC, 2011


import CellEntity
import Bot
import Food
import Grid


class World:

    def __init__(self):
        self._is_game_complete = False
        self._grid = Grid.Grid(32, 32)
        self._blue = []
        self._red  = []
        self._food = []

        map_list = [ # Map class will return this!
            {"type":"RED",  "energy":10, "x":0, "y":0},
            {"type":"RED",  "energy":10, "x":0, "y":1},
            {"type":"RED",  "energy":10, "x":1, "y":0},
            {"type":"RED",  "energy":10, "x":1, "y":1},
            {"type":"BLUE", "energy":10, "x":self._grid.get_x(),
            "y":self._grid.get_y()},
            {"type":"BLUE", "energy":10, "x":self._grid.get_x(),
            "y":self._grid.get_y() - 1},
            {"type":"BLUE", "energy":10, "x":self._grid.get_x() - 1,
            "y":self._grid.get_y()},
            {"type":"BLUE", "energy":10, "x":self._grid.get_x() - 1,
            "y":self._grid.get_y() - 1},
        ]

        for cell in map_list:
            if self._grid.get_cell(cell["x"], cell["y"]):
                print "ERROR: Collision when placing cell", cell

            self._grid.set_cell(cell["x"], cell["y"], cell["type"])
            bot = Bot.Bot(cell["x"], cell["y"], cell["energy"])

            if   cell["type"] == "RED":
                self._red.append(bot)
            elif cell["type"] == "BLUE":
                self._blue.append(bot)
            elif cell["type"] == "FOOD":
                self._food.append(bot)

    def is_game_complete(self):
        return self._is_game_complete

    """
    set_player_code(playerID, path)
        # Set player code

    prepare_world()
        self.grid = Grid(x, y)
        grid.place(TYPE, x, y)



    get_game_state()
        # Return game state i.e. what it looks like and contains.
        # rename to dump_grid()?

    get_game_results()
        # Return:
        # {
        #   'winner':<winner-playerID OR MAX_TURNS_FLAG OR None>,
        #   <playerID>:
        #       {'units':<number of cells occupied>,
        #        'energy':<sum of energy of units> }
        # }
        # Repeat for all playerIDs

    propose_moves(playerID)
        # User code proposes moves for all its bots.
        # For bot in Player's Bot list:
        #   grid.get_neighborhood(bot, VIEW_RADIUS)
        #   use as env variables for player-code
        #   Run player-code for bot
        #   Save bots proposed actions
        # For bot in same-players Bot list:
        #   Apply move
        #   Move/replace


    apply_moves(playerID)
        Would apply moves to Grid and resolve conflicts.
    """


def main():
    world = World()


if __name__ == "__main__":
    main()
