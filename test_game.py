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

        class Decision:

            @staticmethod
            def stochastic(actions):
                action_list = [*actions]
                return action_list[random.randint(0, len(action_list) - 1)]

            @staticmethod
            def choose_min(actions):
                return min(actions)

            @staticmethod
            def choose_max(actions):
                return max(actions)

        Behavior = Decision.choose_min

        def __init__(self, name=None):
            self.name = name

        def choose(self, state):
            print("{}'s turn: ".format(self.name))
            problem = TicTacToeProblem(state)
            agent = AdversarialSearchAgent(problem)
            choice = TicTacToeGame.AI.Behavior(agent.minimax())
            state.choose(choice)

    def __init__(self, player1=Human(), player2=AI()):
        if type(player1) is type(player2) is TicTacToeGame.AI:
            if player1.name is None:
                player1.name = 'Computer 1'
            if player2.name is None:
                player2.name = 'Computer 2'
        if type(player1) is type(player2) is TicTacToeGame.Human:
            if player1.name is None:
                player1.name = 'Player 1'
            if player2.name is None:
                player2.name = 'Player 2'
        if type(player1) is not type(player2):
            if player1.name is None:
                if type(player1) is TicTacToeGame.AI:
                    player1.name = 'Computer'
                else:
                    player1.name = 'Player'
            if player2.name is None:
                if type(player2) is TicTacToeGame.AI:
                    player2.name = 'Computer'
                else:
                    player2.name = 'Player'
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


game = TicTacToeGame(TicTacToeGame.Human(), TicTacToeGame.AI())
game.start()
