#!/usr/bin/env python3.5

from tic_tac_toe import *

name = input('Please Enter Your Name: ')
if name == '':
    name = None
game = TicTacToeGame(TicTacToeGame.Human(name=name),
                     TicTacToeGame.AI(behavior=TicTacToeGame.AI.Decision.choose_min,
                                      algorithm=TicTacToeGame.AI.Algorithm.exact))
game.start()
