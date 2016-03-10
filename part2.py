#!/usr/bin/env python3.5

from tic_tac_toe import *

game = TicTacToeGame(TicTacToeGame.AI(behavior=TicTacToeGame.AI.Decision.choose_min,
                                      algorithm=TicTacToeGame.AI.Algorithm.approximate),
                     TicTacToeGame.AI(behavior=TicTacToeGame.AI.Decision.choose_min,
                                      algorithm=TicTacToeGame.AI.Algorithm.approximate))
game.start()
