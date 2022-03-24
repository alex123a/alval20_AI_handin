global TOTAL_LENGTH
TOTAL_LENGTH = 0

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
I only send the children with the shortest length
'''
def successor_fn(state):  # Lookup list of successor states
    global TOTAL_LENGTH

    temp_total_length = TOTAL_LENGTH
    children = STATE_SPACE[state]
    best_route_dic = {'location': children[0]['location'], 'length': children[0]['length'], 'h': children[0]['h']}
    temp = temp_total_length + best_route_dic['length'] + best_route_dic['h']
    temp_length = 0
    temp_index = 0
    for i in range(1, len(children)):
        # TODO update length on the state_space, so when it goes to B, B's length change to the total_length
        
        temp_length = temp_total_length + children[i]['length']
        temp_length_with_h = temp_length + children[i]['h']
        if (temp_length_with_h < temp and children[i]['location'] != GOAL_STATE):
            temp_index = i
            best_route_dic = children[i]
            temp = temp_length + children[i]['h']
        elif (children[i]['location'] == GOAL_STATE and best_route_dic['location'] != GOAL_STATE):
            temp_index = i
            best_route_dic = children[i]
            temp = temp_length + children[i]['h']
        elif (children[i]['location'] == GOAL_STATE and best_route_dic['location'] == GOAL_STATE and temp_length_with_h < temp):
            temp_index = i
            best_route_dic = children[i]
            temp = temp_length + children[i]['h']
    
    TOTAL_LENGTH = temp_total_length + best_route_dic['length']
    if (STATE_SPACE[state][temp_index]['location'] != GOAL_STATE):
        STATE_SPACE[state][temp_index] = {'location': best_route_dic['location'], 'length': temp_total_length + best_route_dic['length'], 'h': best_route_dic['h']}
    return best_route_dic['location']
    

# W is not across and E is across/sailing
INITIAL_STATE = 'A'
GOAL_STATE = 'L' or 'K'
# (Farmer status, Goat status, Cabbage status, Wolf status)
STATE_SPACE = {
    'A': [{'location': 'B', 'length': 1, 'h': 5}, {'location': 'C', 'length': 2, 'h': 5}, {'location': 'D', 'length': 4, 'h': 2}],
    'B': [{'location': 'F', 'length': 5, 'h': 5}, {'location': 'E', 'length': 4, 'h': 4}],
    'C': [{'location': 'E', 'length': 1, 'h': 4}, {'location': 'A', 'length': 2, 'h': 6}],
    'D': [{'location': 'H', 'length': 1, 'h': 1}, {'location': 'I', 'length': 4, 'h': 2}, {'location': 'J', 'length': 2, 'h': 1}],
    'F': [{'location': 'G', 'length': 1, 'h': 4}, {'location': 'B', 'length': 5, 'h': 5}],
    'E': [{'location': 'G', 'length': 2, 'h': 4}, {'location': 'H', 'length': 3, 'h': 1}],
    'H': [{'location': 'K', 'length': 6, 'h': 0}, {'location': 'L', 'length': 5, 'h': 0}],
    'I': [{'location': 'L', 'length': 3, 'h': 0}],
    'J': [{'location': 'D', 'length': 2, 'h': 2}],
    'G': [{'location': 'K', 'length': 6, 'h': 0}],
    'K': [],
    'L': []
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
