from tic_tac_toe import *

game = TicTacToeGame(TicTacToeGame.AI(behavior=TicTacToeGame.AI.Decision.stochastic,
                                      algorithm=TicTacToeGame.AI.Algorithm.approximate),
                     TicTacToeGame.AI(behavior=TicTacToeGame.AI.Decision.stochastic,
                                      algorithm=TicTacToeGame.AI.Algorithm.approximate))
game.start()
