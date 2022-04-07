import random

def decision(state):
    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for s in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for s in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action = argmax(successors_of(state), lambda a: min_value(a))
    return action
    
    '''
    if is_terminal(state):
        return utility_of(state)
    successors = successors_of(state)
    action = successors[random.randint(0, len(successors) - 1)]
    '''
    
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    print(f'What is the state given as parameter in is_terminal?: {state}')
    # Checking if there is an avaible move.
    done = True
    for i in state:
        if (i > 2):
            done = False
    return done


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: Sta+te of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    if (len(state) % 2 == 0):
        return -1
    else:
        return 1

def successors_of(state):

    index_accepted = []
    for i in range(0, len(state)):
        if state[i] > 2:
            index_accepted.append(i)

    successors = []
    for i in index_accepted:
        for j in range(1, state[i] // 2 + 1):
            temp = state[:]
            if (temp[i] - j == j):
                break
            temp[i] = temp[i] - j
            temp.append(j)
            successors.append((temp))

    return successors

def computer_select_pile(state):
    # new_state = alpha_beta.alpha_beta_decision(state)
    new_state = decision(state)
    return new_state


def user_select_pile(list_of_piles):
    '''
    Given a list of piles, asks the user to select a pile and then a split.
    Then returns the new list of piles.
    '''
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("Which pile (from 1 to {}, must be > 2)?".format(len(list_of_piles)))
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        if list_of_piles[i] % 2 == 0:
            print(
                'How much is the first split (from 1 to {}, but not {})?'.format(
                    max_split,
                    list_of_piles[i] // 2
                )
            )
        else:
            print(
                'How much is the first split (from 1 to {})?'.format(max_split)
            )
        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1:]

    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles


def main():
    state = [15]

    while not is_terminal(state):
        state = user_select_pile(state)
        if not is_terminal(state):
            state = computer_select_pile(state)

    print("    Final state is {}".format(state))

'''
def display(state):
    print("-----")
    # TODO Rewrite this part so it shows avaible splits
    print(state)


def main():
    global player_turn
    board = [15]
    print(f'Starting board: {board}')
    print(f'AI begins')
    print('----------------')
    player_turn = True
    while not is_terminal(board):
        player_turn = False
        # board = decision(board)
        board = alpha_beta.alpha_beta_decision(board)
        if not is_terminal(board):
            player_turn = True
            succesors = successors_of(board)
            display(succesors)
            board = succesors[int(input('Your move (select choice)? ')) - 1]
    display(board)
    print('----------------')
    if player_turn:
        print("Human player won!")
    else:
        print("AI won!")
'''


def argmax(iterable, func):
    return max(iterable, key=func)



if __name__ == '__main__':
    main()
