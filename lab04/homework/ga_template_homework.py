import random
import math
from queens_fitness import *


p_mutation = 0.2
num_of_generations = 30


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)
            child2 = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)
            if random.uniform(0, 1) < p_mutation:
                child2 = mutate(child2)

            new_population.add(child)
            new_population.add(child2)

            ordered_population = list(new_population)

            total_fitness = 0
            for individuel in ordered_population:
                total_fitness += fitness_fn(individuel)

            for i in ordered_population:
                if fitness_fn(i) < total_fitness/len(ordered_population): 
                    new_population.remove(i)

        # Add new population to population, use union to disregard duplicate individuals
        population = population.union(new_population)

        fittest_individual = get_fittest_individual(population, fitness_fn)

        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    '''
    Reproduce two individuals with single-point crossover
    Return the child individual
    '''
    # If 0 it will only choose the fathers and if 3 it will only choose the mother
    crossover_point = random.randint(0, len(father))
    child = []
    for i in range(0, crossover_point):
        child.append(mother[i])
    
    for i in range(crossover_point, len(father)):
        child.append(father[i])

    return tuple(child)


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''

    mutation = list(individual)
    index = random.randint(0, len(individual) - 1)
    random_number = -1
    notAllowed = True
    while (notAllowed):
        random_number = random.randint(0, 8)
        if (random_number != mutation[index]):
            notAllowed = False
        
        for i in mutation:
            if (random_number == i):
                notAllowed = True
                break

    mutation[index] = random_number
        
    return tuple(mutation)
    

def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)
    
    total_fitness = 0
    for individuel in ordered_population:
        total_fitness += fitness_fn(individuel)

    selected = []
    population_fitness = []

    for i in ordered_population:
        population_fitness.append((((fitness_fn(i) / total_fitness) * 100), i))

    population_fitness.sort()

    selected = []
    counter = 0
    to_be_selected = random.randint(0, 99)
    for i in range(0, len(population_fitness)):
        counter += population_fitness[i][0]
        if (counter >= to_be_selected):
            selected.append(population_fitness[i][1])
            break
    
    counter = 0
    to_be_selected = random.randint(0, 99)
    for i in population_fitness:
        counter += i[0]
        if (counter >= to_be_selected):
            selected.append(i[1])
            break

    return selected
    


def fitness_function(individual):
    '''
    Computes the decimal value of the individual
    Return the fitness level of the individual

    Explanation:
    enumerate(list) returns a list of pairs (position, element):

    enumerate((4, 6, 2, 8)) -> [(0, 4), (1, 6), (2, 2), (3, 8)]

    enumerate(reversed((1, 1, 0))) -> [(0, 0), (1, 1), (2, 1)]
    '''
    return fitness_fn_negative(individual)


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''

    '''
    return set([
        tuple(random.randint(0, 1) for _ in range(n))
        for _ in range(count)
    ])
    '''
    numbers = [0, 1, 2, 3, 4, 5, 6, 7]
    random.shuffle(numbers)
    return set([
        tuple(numbers)
    ])


def main():
    minimal_fitness = 7

    # Curly brackets also creates a set, if there isn't a colon to indicate a dictionary
    '''
    initial_population = {
        (2, 4, 7, 4, 8, 5, 5, 2),
        (3, 2, 7, 5, 2, 4, 1, 1),
        (2, 4, 4, 1, 5, 1, 2, 4),
        (3, 2, 5, 4, 3, 2, 1, 3)
    }
    '''
    initial_population = get_initial_population(8, 4)

    fittest = genetic_algorithm(initial_population, fitness_function, minimal_fitness)
    print('Fittest Individual: ' + str(fittest) + ' minimal fitness ' + str(fitness_fn_negative(fittest)))


if __name__ == '__main__':
    pass
    main()
