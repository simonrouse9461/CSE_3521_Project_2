class ProblemFormulation:

    def __init__(self, initial_state):
        self.initial_state = initial_state

    @classmethod
    def actions(cls, state):
        raise NotImplementedError

    @classmethod
    def result(cls, state, action):
        raise NotImplementedError

    @classmethod
    def player(cls, state):
        raise NotImplementedError

    @classmethod
    def terminal_test(cls, state):
        raise NotImplementedError

    @classmethod
    def utility(cls, state, player):
        raise NotImplementedError

    @classmethod
    def eval(cls, state, player):
        raise NotImplementedError


class AdversarialSearchAgent:

    def __init__(self, problem):
        if not issubclass(type(problem), ProblemFormulation):
            raise TypeError('Subclass of ProblemFormulation expected!')
        self.problem = problem

    def __max_utility_actions(self, state, player):
        if self.problem.terminal_test(state):
            return self.problem.utility(state, player), set()
        utility_map = dict()
        best_set = set()
        max_utility = None
        for action in self.problem.actions(state):
            result = self.problem.result(state, action)
            min_utility, _ = self.__min_utility_actions(result, player)
            utility_map[action] = min_utility
            if max_utility is None:
                max_utility = min_utility
            elif max_utility < min_utility:
                max_utility = min_utility
        for action, utility in utility_map.items():
            if utility == max_utility:
                best_set.add(action)
        return max_utility, best_set

    def __min_utility_actions(self, state, player):
        if self.problem.terminal_test(state):
            return self.problem.utility(state, player), set()
        utility_map = dict()
        best_set = set()
        min_utility = None
        for action in self.problem.actions(state):
            result = self.problem.result(state, action)
            max_utility, _ = self.__max_utility_actions(result, player)
            utility_map[action] = max_utility
            if min_utility is None:
                min_utility = max_utility
            elif min_utility > max_utility:
                min_utility = max_utility
        for action, utility in utility_map.items():
            if utility == min_utility:
                best_set.add(action)
        return min_utility, best_set

    def minimax(self):
        return self.__max_utility_actions(self.problem.initial_state,
                                          self.problem.player(self.problem.initial_state))
