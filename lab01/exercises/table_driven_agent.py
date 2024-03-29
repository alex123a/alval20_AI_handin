A = 'A'
B = 'B'
percepts = []
table = {
    ((A, 'Clean'), ): 'Right',
    ((A, 'Dirty'), ): 'Suck',
    ((B, 'Clean'), ): 'Left',
    ((B, 'Dirty'), ): 'Suck',
    ((A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Dirty')): 'Suck',
    ((B, 'Clean'), (A, 'Clean')): 'Left',
    ((B, 'Clean'), (A, 'Dirty')): 'Suck',
    ((A, 'Clean'), (A, 'Clean'), (A, 'Clean')): 'Right',
    ((A, 'Clean'), (A, 'Clean'), (A, 'Dirty')): 'Suck',
    ((A, 'Clean'), (A, 'Dirty'), (B, 'Clean')): 'Left',
}

def lookup(percept, table):
    action = table.get(tuple(percept))
    return action

def table_driven_agent(percept):
    percepts.append(percept)
    action = lookup(percepts, table)
    return action

def run():
    print('Action\tPercepts')
    print(table_driven_agent((A, 'Clean')), '\t', percepts)
    print(table_driven_agent((A, 'Dirty')), '\t', percepts)
    print(table_driven_agent((B, 'Clean')), '\t', percepts)

run()