from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.recursive_backtracking(assignment)
                if result:
                    return result
                assignment.pop(var)
        return False



    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_australia_csp():
    cr, pan, co, ven, guya, sur, guyaFR, bra, ecu, per, boli, para, chile, arg, uru = "cr", "pan", "co", "ven", "guya", "sur", "guyaFR", "bra", "ecu", "per", "boli", "para", "chile", "arg", "uru"
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [cr, pan, co, ven, guya, sur, guyaFR, bra, ecu, per, boli, para, chile, arg, uru]
    domains = {
        cr: values[:],
        pan: values[:],
        co: values[:],
        ven: values[:],
        guya: values[:],
        sur: values[:],
        guyaFR: values[:],
        bra: values[:],
        ecu: values[:],
        per: values[:],
        boli: values[:],
        para: values[:],
        chile: values[:],
        arg: values[:],
        uru: values[:]
    }
    neighbours = {
        cr: [pan],
        pan: [cr, co],
        co: [pan, ven, ecu, per, bra],
        ven: [co, bra, guya],
        guya: [ven, sur, bra],
        sur: [guya, guyaFR, bra],
        guyaFR: [sur, bra],
        bra: [co, ven, guya, sur, guyaFR, per, boli, para, arg, uru],
        ecu: [co, per],
        per: [ecu, co, boli, chile, bra],
        boli: [per, bra, para, arg, chile],
        para: [boli, bra, arg],
        chile: [per, boli, arg],
        arg: [chile, boli, para, bra, uru],
        uru: [arg, bra]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        cr: constraint_function,
        pan: constraint_function,
        co: constraint_function,
        ven: constraint_function,
        guya: constraint_function,
        sur: constraint_function,
        guyaFR: constraint_function,
        bra: constraint_function,
        ecu: constraint_function,
        per: constraint_function,
        boli: constraint_function,
        para: constraint_function,
        chile: constraint_function,
        arg: constraint_function,
        uru: constraint_function
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    australia = create_australia_csp()
    result = australia.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
