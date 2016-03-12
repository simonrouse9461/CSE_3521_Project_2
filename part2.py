#!/usr/bin/env python3.5

from tic_tac_toe import *

game = TicTacToeGame(AI(behavior=AI.Decision.choose_min,
                        algorithm=AI.Algorithm.approximate),
                     AI(behavior=AI.Decision.choose_min,
                        algorithm=AI.Algorithm.approximate))
game.start()
