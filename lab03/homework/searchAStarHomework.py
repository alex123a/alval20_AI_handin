from random import randint

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
        if (SQUARES_STATUS != GOAL_STATE):
            return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)
        else:
            return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH) + ' - Total cost: ' + str(TOTAL_LENGTH)

'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_FIRST(fringe)
        if SQUARES_STATUS == GOAL_STATE:
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
    if (SQUARES_STATUS == GOAL_STATE):
        return None
    temp_total_length = TOTAL_LENGTH
    children = STATE_SPACE[state]
    best_route_dic = {'tile': children[0]['tile'], 'length': children[0]['length'], 'h': children[0]['h']}
    temp = temp_total_length + best_route_dic['length'] + best_route_dic['h']
    temp_length = 0
    temp_index_parent = 0
    temp_index = 0
    for i in range(1, len(children)):
        # if children[i]['tile'] == state:
        #     STATE_SPACE[state][i] = {'tile': children[i]['tile'], 'length': temp_total_length + children[i]['length'], 'h': children[i]['h']}
        
        temp_length = temp_total_length + children[i]['length']
        temp_length_with_h = temp_length + children[i]['h']
        if (temp_length_with_h < temp):
            temp_index = i
            best_route_dic = children[i]
            temp = temp_length + children[i]['h']
    
    TOTAL_LENGTH = temp_total_length + best_route_dic['length']
    STATE_SPACE[state][temp_index] = {'tile': best_route_dic['tile'], 'length': 1 + temp_total_length + best_route_dic['length'], 'h': best_route_dic['h']}
    # The if statement checks if it is the same tile again. If it is then it cleans.
    if best_route_dic['tile'] == state:
        SQUARES_STATUS[SQUARES_INDEX[state]] = 'Clean'
    # print(SQUARES_STATUS)
    return best_route_dic['tile']
    

# W is not across and E is across/sailing
SQUARES = ['A', 'B', 'C', 'D']
SQUARES_INDEX = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
# A, B, C, D
SQUARES_STATUS = ['Dirty', 'Dirty', 'Dirty', 'Dirty']
INITIAL_STATE = SQUARES[randint(0, 3)]
GOAL_STATE = ['Clean', 'Clean', 'Clean', 'Clean']
# 
STATE_SPACE = {
    # Every list contains the same tile again (if this is chosen it will be cleaned) and the two tiles it can move to
    # I don't have "do nothing"
    'A': [{'tile': 'A', 'length': 1, 'h': 0}, {'tile': 'B', 'length': 5, 'h': 0}, {'tile': 'C', 'length': 6, 'h': 0}],
    'B': [{'tile': 'B', 'length': 1, 'h': 0}, {'tile': 'A', 'length': 5, 'h': 0}, {'tile': 'D', 'length': 6, 'h': 0}],
    'C': [{'tile': 'C', 'length': 1, 'h': 0}, {'tile': 'D', 'length': 5, 'h': 0}, {'tile': 'A', 'length': 6, 'h': 0}],
    'D': [{'tile': 'D', 'length': 1, 'h': 0}, {'tile': 'C', 'length': 5, 'h': 0}, {'tile': 'B', 'length': 6, 'h': 0}],
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
