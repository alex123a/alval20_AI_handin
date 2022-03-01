from random import randint

A = 'A'
B = 'B'
C = 'C'
D = 'D'
state = {}
action = None
model = {A: None, B: None, C: None, D: None}
squares = [A, B, C, D]

RULE_ACTION = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp',
    5: 'Up',
    6: 'Down'
}

rules = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (C, 'Dirty'): 1,
    (D, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 6,
    (C, 'Clean'): 3,
    (D, 'Clean'): 5,
    (A, B, C, D, 'Clean'): 4,
}

environment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Clean',
    D: 'Dirty',
    'Current': squares[randint(0, 3)]
}

def interpret_input(input):
    return input

def rule_match(state, rules):
    rule = rules.get(tuple(state))
    return rule

def update_state(state, action, percept):
    (location, status) = percept
    state = percept
    if model[A] == model[B] == model[C] == model[D] =='Clean':
        state = (A, B, C, D, 'Clean')
    model[location] = status
    return state

def reflex_agent_with_state(percept):
    global state, action
    state = update_state(state, action, percept)
    rule = rule_match(state, rules)
    action = RULE_ACTION[rule]
    return action

def sensors():
    location = environment['Current']
    return (location, environment[location])

def actuators(action):
    location = environment['Current']
    if action == 'Suck':
        environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        environment['Current'] = B
    elif action == 'Down' and location == B:
        environment['Current'] = C
    elif action == 'Left' and location == C:
        environment['Current'] = D
    elif action == 'Up' and location == D:
        environment['Current'] = A

def run(n):
    print('     Current\t\t\t   New')
    print('location status\t\taction\t location    status')
    for i in range(1, n):
        (location, status) = sensors()
        print("{:10s}{:15s}".format(location, status), end='')
        action = reflex_agent_with_state(sensors())
        actuators(action)
        (location, status) = sensors()
        print("{:11s}{:9s}{:8s}".format(action, location, status))

run(20)