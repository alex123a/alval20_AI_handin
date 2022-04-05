import random

def decision(state):
    if is_terminal(state):
        return utility_of(state)
    successors = successors_of(state)
    action = successors[random.randint(0, len(successors) - 1)]
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
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

    if (player_turn):
        return 1
    else:
        return -1


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

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
        board = decision(board)
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


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
