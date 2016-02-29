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

    def __iter__(self):
        for i in (0, 1, 2):
            yield self.__list[i], self.__list[i + 3], self.__list[i + 6]
        for i in (0, 3, 6):
            yield self.__list[i], self.__list[i + 1], self.__list[i + 2]
        for i in (0,):
            yield self.__list[i], self.__list[i + 4], self.__list[i + 8]
        for i in (2,):
            yield self.__list[i], self.__list[i + 2], self.__list[i + 4]

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

    @property
    def copy(self):
        copy = TicTacToe()
        copy.player = self.player
        copy.__list = [*self.__list]
        copy.history = [*self.history]
        return copy

    @property
    def available_actions(self):
        actions = set()
        for action in TicTacToe.all_actions:
            if self.winner is None and self.can_choose(action):
                actions.add(action)
        return actions

    @property
    def winner(self):
        for first, second, third in self:
            if first == second == third != 0:
                return first
        for i in self.__list:
            if i == 0:
                return None
        return 0

    def can_choose(self, position):
        if not 1 <= position <= 9:
            return False
        return self.__list[position - 1] == 0

    def choose(self, position):
        if self.can_choose(position):
            self.__list[position - 1] = self.player
            self.history += [(self.player, position)]
            self.player = 3 - self.player

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
        x1, x2, o1, o2 = [0] * 4
        for first, second, third in state:

            p_count = 0
            a_count = 0

