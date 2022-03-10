class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_FIRST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    queue.append(node)
    return queue


'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for i in list:
        queue.append(i)
    return queue


'''
Removes and returns the first element from fringe
'''
def REMOVE_FIRST(queue):
    element = queue[0]
    queue.remove(queue[0])
    return element

'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    # I only send the children with the shortest length
    # This should probably be in another method
    best_route = ('Placeholder', 100000000000000)
    for i in STATE_SPACE[state]:
        if (i[1] < best_route[1]):
            best_route = i

    return [best_route]
    

# W is not across and E is across/sailing
INITIAL_STATE = ('A', 6)
GOAL_STATE = ('K', 0) or ('L', 0)
# (Farmer status, Goat status, Cabbage status, Wolf status)
STATE_SPACE = {
    ('A', 6): [('B', 5), ('C', 5), ('D', 2)],
    ('B', 5): [('F', 5), ('E', 4), ('A', 6)],
    ('C', 5): [('E', 4), ('A', 6)],
    ('D', 2): [('H', 1), ('I', 2), ('J', 1), ('A', 6)],
    ('F', 5): [('G', 4), ('B', 5)],
    ('E', 4): [('G', 4), ('H', 1), ('B', 5), ('C', 5)],
    ('H', 1): [('E', 4), ('D', 2), ('K', 0), ('L', 0)],
    ('I', 2): [('D', 2), ('L', 0)],
    ('J', 1): [('D', 2)],
    ('G', 4): [('F', 5), ('E', 4), ('K', 0)],
    ('K', 0): [],
    ('L', 0): []


}


'''
Run tree search and display the nodes in the path to goal node
'''
def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
