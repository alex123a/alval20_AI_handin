from random import randint

A = 'A'
B = 'B'
C = 'C'
D = 'D'

squares = [A, B, C, D]

enviroment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Clean',
    D: 'Dirty',
    'Current': squares[randint(0, 3)]
}

def reflex_vacuum_agent(loc_st):
    if loc_st[1] == 'Dirty':
        return 'Suck'
    if loc_st[0] == A:
        return 'Right'
    if loc_st[0] == B:
        return 'Down'
    if loc_st[0] == C:
        return 'Left'
    if loc_st[0] == D:
        return 'Up'

def sensors():
    location = enviroment['Current']
    return (location, enviroment[location])

def actuators(action):
    location = enviroment['Current']
    if action == 'Suck':
        enviroment[location] = 'Clean'
    elif action == 'Right' and location == A:
        enviroment['Current'] = B
    elif action == 'Down' and location == B:
        enviroment['Current'] = C
    elif action == 'Left' and location == C:
        enviroment['Current'] = D
    elif action == 'Up' and location == D:
        enviroment['Current'] = A
    

def run(n):
    print('     Current\t\t\t   New')
    print('location status\t\taction\t location    status')
    for i in range(1, n):
        (location, status) = sensors()
        print("{:10s}{:15s}".format(location, status), end='')
        action = reflex_vacuum_agent(sensors())
        actuators(action)
        (location, status) = sensors()
        print("{:11s}{:9s}{:8s}".format(action, location, status))

run(20)