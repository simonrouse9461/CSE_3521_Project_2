import random
from adversarial_search_agent import *


class TicTacToe:

    all_actions = [*range(1, 10)]

    def __init__(self):
        self.player = 1
        self.__list = [0] * 9
        self.history = []

    def __str__(self):
        format_str = '\n+---+---+---+\n| {} | {} | {} |' * 3 + '\n+---+---+---+\n'
        return format_str.format(*self.tuple)

    def __eq__(self, other):
        return self.__list == other.__list

    # iterate through all possible lines
    def __iter__(self):
        for i in (0, 1, 2):
            yield self.__list[i], self.__list[i + 3], self.__list[i + 6]
        for i in (0, 3, 6):
            yield self.__list[i], self.__list[i + 1], self.__list[i + 2]
        for i in (0,):
            yield self.__list[i], self.__list[i + 4], self.__list[i + 8]
        for i in (2,):
            yield self.__list[i], self.__list[i + 2], self.__list[i + 4]

    # return a tuple representation of current state
    @property
    def tuple(self):
        temp_list = [*range(1, 10)]
        if self.__list == [0] * 9:
            return tuple(temp_list)
        for i, player in enumerate(self.__list):
            if player == 0:
                temp_list[i] = ' '
            if player == 1:
                temp_list[i] = 'X'
            if player == 2:
                temp_list[i] = 'O'
        return tuple(temp_list)

    # return a deep copy
    @property
    def copy(self):
        copy = TicTacToe()
        copy.player = self.player
        copy.__list = [*self.__list]
        copy.history = [*self.history]
        return copy

    # return all available actions under current state
    @property
    def available_actions(self):
        actions = set()
        for action in TicTacToe.all_actions:
            if self.winner is None and self.can_choose(action):
                actions.add(action)
        return actions

    # return winner, 0 means tie. If there is no winner yet, return None.
    @property
    def winner(self):
        for first, second, third in self:
            if first == second == third != 0:
                return first
        for i in self.__list:
            if i == 0:
                return None
        return 0

    # check if a position is choosable
    def can_choose(self, position):
        if not 1 <= position <= 9:
            return False
        return self.__list[position - 1] == 0

    # choose a position
    def choose(self, position):
        if self.can_choose(position):
            self.__list[position - 1] = self.player
            self.history += [(self.player, position)]
            self.player = 3 - self.player

    # undo one step
    def undo(self):
        if len(self.history) == 0:
            return
        self.__list[self.history.pop(-1)[1] - 1] = 0
        self.player = 3 - self.player


class TicTacToeProblem(ProblemFormulation):

    def __init__(self, initial_state=TicTacToe()):
        super(TicTacToeProblem, self).__init__(initial_state)
        self.initial_state = initial_state.copy

    @classmethod
    def actions(cls, state):
        return state.available_actions

    @classmethod
    def result(cls, state, action):
        copy = state.copy
        copy.choose(action)
        return copy

    @classmethod
    def player(cls, state):
        return state.player

    @classmethod
    def terminal_test(cls, state):
        return state.winner is not None

    @classmethod
    def utility(cls, state, player):
        return state.winner if state.winner == 0 or state.winner is None else 10 if state.winner == player else -10

    @classmethod
    def eval(cls, state, player):
        p1, p2, a1, a2 = [0] * 4
        for line in state:
            p_count = line.count(player)
            a_count = line.count(3 - player)
            if p_count == 2 and a_count == 0:
                p2 += 1
            if p_count == 1 and a_count == 0:
                p1 += 1
            if p_count == 0 and a_count == 2:
                a2 += 1
            if p_count == 0 and a_count == 1:
                a1 += 1
        return 3 * p2 + p1 - (3 * a2 + a1)


class TicTacToeGame:

    class Human:

        def __init__(self, name=None):
            self.name = name

        def choose(self, state):
            try:
                choose_number = int(input("{}'s turn: ".format(self.name)))
            except:
                choose_number = None
            while choose_number is None or not state.can_choose(choose_number):
                print('invalid input number, please input again.\n')
                try:
                    choose_number = int(input("{}'s turn: ".format(self.name)))
                except:
                    choose_number = None
            state.choose(choose_number)

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

        class Algorithm:

            @staticmethod
            def exact(agent):
                return agent.minimax_search()[1], agent.minimax_values()

            @staticmethod
            def approximate(agent):
                return agent.h_minimax_search()[1], agent.h_minimax_values()

        def __init__(self, name=None, behavior=Decision.choose_min, algorithm=Algorithm.exact):
            self.name = name
            self.behavior = behavior
            self.algorithm = algorithm

        def choose(self, state):
            print("{}'s turn: ".format(self.name))
            problem = TicTacToeProblem(state)
            agent = AdversarialSearchAgent(problem)
            evaluations = self.algorithm(agent)[1]
            print("evaluations:", evaluations)
            choice = self.behavior(self.algorithm(agent)[0])
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

