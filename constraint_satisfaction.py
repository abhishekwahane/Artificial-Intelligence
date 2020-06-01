# PB1 ABHISHEK WAHANE
# Constraint Satisfaction Problem


class Constraint:
    def __init__(self, letters):
        self.letters = letters

    def satisfied(self, assignment):
        if len(set(assignment.values())) < len(assignment):
            return False

        if len(assignment) == len(self.letters):
            # Assigned values
            s = assignment['S']
            e = assignment['E']
            n = assignment['N']
            d = assignment['D']
            m = assignment['M']
            o = assignment['O']
            r = assignment['R']
            y = assignment['Y']

            # Checking if condition is satisfied
            send = s * 1000 + e * 100 + n * 10 + d
            more = m * 1000 + o * 100 + r * 10 + e
            money = m * 10000 + o * 1000 + n * 100 + e * 10 + y

            return send + more == money
        return True


class CSP:
    def __init__(self, variables, domain):
        self.variables = variables
        self.domain = domain
        self.constraints = {}

        for var in self.variables:
            self.constraints[var] = []
            if var not in self.domain:
                print('Domain Assignment Error')
                raise LookupError("Domain Assignment Error")

    def add_constraint(self, constraint):
        for v in constraint.letters:
            if v not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[v].append(constraint)

    def consistent(self, variable, assignment):
        # Checking all the constraints
        for cons in self.constraints[variable]:
            if not cons.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment={}):
        '''To run a backtracking algorithm with constraints'''
        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]
        for value in self.domain[first]:
            # print(self.domain[first])
            local_assignment = assignment.copy()
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                # print(local_assignment)
                # print()
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None


letters = list("SENDMORY")
possible_digits = {}
for l in letters:
    possible_digits[l] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

possible_digits["M"] = [1]
csp = CSP(letters, possible_digits)
csp.add_constraint(Constraint(letters))
result = csp.backtracking_search()
if result is None:
    print("No Solution Found.")
else:
    print(result)

"""

OUTPUT:

# {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}

"""
