from game import *

game = TicTacToeGame(TicTacToeGame.AI(algorithm=TicTacToeGame.AI.Algorithm.approximate),
                     TicTacToeGame.AI(algorithm=TicTacToeGame.AI.Algorithm.approximate))
game.start()
