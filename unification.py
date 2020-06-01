# PB1 ABHISHEK WAHANE
# Unification Algorithm


class Variable:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class Constant:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value


class Relation:
    def __init__(self, name, args):
        self.name = name
        self.value = str(self.name) + str([i.value for i in args])
        self.args = args


def unification(L1, L2, testset):

    if (isinstance(L1, Variable) or isinstance(L2, Variable) or isinstance(L1, Constant) or isinstance(L2, Constant)):
        if L1 == L2:
            return None
        elif isinstance(L1, Variable):
            if isinstance(L2, Variable):
                print('Mismatching variables!')
                return False
            else:
                if L1.value not in testset.values():
                    return [L2, L1]
                else:
                    print('Ambiguous Variable.')
                    return False
        elif isinstance(L2, Variable):
            if isinstance(L1, Variable):
                print('Mismatching Variables!')
                return False
            else:
                if L2.value not in testset.values():
                    return [L1, L2]
                else:
                    print('Ambiguous Variable')
                    return False
        else:
            print('Mismatch!!')
            return False

    elif L1.name != L2.name:
        print('Relation does not match')
        return False

    elif len(L1.args) != len(L2.args):
        print('Number of Arguments do not match')
        return False

    subset = {}

    for i in range(len(L1.args)):
        s = unification(L1.args[i], L2.args[i], subset)
        if s == False:
            return False
        if s != None:
            subset[s[0].value] = s[1].value

    return subset


print('Unification:\n')

print(unification(Relation('Knows', [Constant('John'), Variable('X')]), Relation(
    'Knows', [Variable('Y'), Relation("Brother", [Variable("Y")])]), {}))

print(unification(Relation("Knows", [Constant("Ram"), Variable("X")]), Relation(
    "Knows", [Variable("Y"), Constant("Shyam")]), {}))


"""

OUTPUT:

Unification:

{'John': 'Y', "Brother['Y']": 'X'}
{'Ram': 'Y', 'Shyam': 'X'}

"""
