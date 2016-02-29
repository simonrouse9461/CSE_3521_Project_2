import random
from tic_tac_toe import *
from adversarial_search_agent import *


class TicTacToeGame:

    class Human:

        def __init__(self, name=None):
            self.name = name

        def choose(self, state):
            state.choose(int(input("{}'s turn: ".format(self.name))))

    class AI:

        def __init__(self, name=None):
            self.name = name

        def choose(self, state):
            print("{}'s turn: ".format(self.name))
            problem = TicTacToeProblem(state)
            agent = AdversarialSearchAgent(problem)
            action_list = [*agent.minimax()[1]]
            choice = action_list[random.randint(0, len(action_list) - 1)]
            state.choose(choice)

    def __init__(self, player1=Human(), player2=AI()):
        if player1.name is None:
            player1.name = 'Player1'
        if player2.name is None:
            player2.name = 'Player2'
        self.player1 = player1
        self.player2 = player2
        self.state = TicTacToe()

    def turn(self, player):
        player.choose(self.state)
        print(self.state)
        return self.terminal_test()

    def terminal_test(self):
        if self.state.winner == 0:
            print('Tie!')
            return True
        if self.state.winner == 1:
            print('{} win!'.format(self.player1.name))
            return True
        if self.state.winner == 2:
            print('{} win!'.format(self.player2.name))
            return True
        return False

    def start(self):
        print('Game started!')
        print(self.state)
        while True:
            if self.turn(self.player1):
                break
            if self.turn(self.player2):
                break


game = TicTacToeGame(TicTacToeGame.Human('Simon'), TicTacToeGame.AI('Computer'))
game.start()
