def minmax_decision(state):

    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


def is_terminal(state):
    """
    returns True if the state is either a win or a tie (board full)
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """

    # Checking if tie
    isTie = True
    for i in state:
        if isinstance(i):
            isTie = False
    
    if isTie:
        return True

    # Checking Columns
    for i in range(0, 3):
        if state[i] == state[i + 3] == state[i + 6]:
            return True
        if state[i * 3] == state[i * 3 + 1] == state[i * 3 + 2]:
            return True

    # Checking diagonal
    if state[0] == state[4] == state[8] or state[2] == state[4] == state[6]:
        return True
    
    # Returning False if none of the above are true.
    return False


def utility_of(state):
    """
    returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    # Checking if tie
    isTie = True
    for i in state:
        if isinstance(i):
            isTie = False
    
    if isTie:
        return 0

    # Checking Columns
    for i in range(0, 3):
        if state[i] == state[i + 3] == state[i + 6]:
            return 1 if state[i] == 'X' else -1
        if state[i * 3] == state[i * 3 + 1] == state[i * 3 + 2]:
            return 1 if state[i] == 'X' else -1

    # Checking diagonal
    if state[0] == state[4] == state[8] or state[2] == state[4] == state[6]:
        return 1 if state[i] == 'X' else -1
    
    # Returning False if none of the above are true.
    return 0


def successors_of(state):
    """
    returns a list of tuples (move, state) as shown in the exercise slides
    :param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
    :return:
    """
    pass


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
