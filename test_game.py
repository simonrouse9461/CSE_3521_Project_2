import random
from tic_tac_toe import *
from adversarial_search_agent import *


game = TicTacToe()
print(game)
while True:
    action = int(input('choose: '))
    game.choose(action)
    print(game)
    if game.winner == 1:
        print('You win!')
        break
    elif game.winner == 0:
        print('Tie!')
        break
    problem = TicTacToeProblem(game)
    agent = AdversarialSearchAgent(problem)
    action_list = [*agent.minimax()[1]]
    AI_action = action_list[random.randint(0, len(action_list) - 1)]
    game.choose(AI_action)
    print(game)
    if game.winner == 2:
        print('You lose!')
        break
    elif game.winner == 0:
        print('Tie!')
        break
