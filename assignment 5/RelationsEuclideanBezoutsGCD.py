'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
EECS210 Assignment 5
Description:
A program written to do multiple problems involving relations, gcd, Euclidean algorithms, and Bézout's coefficients
Collaborators: None
Sources: ChatGPT
Full Name: Tuan Vu
Creation Date: 10/26/2023
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

print('-------------------PROGRAM 1-------------------')

def is_function(relation):
    '''
    Function Checker

    Inputs:
        list

    Ouputs:
        boolean value
    '''

    # Init variables (sets)
    domain = set()
    codomain = set()

    # For all elements in the domain, are the elements assigned to only one other element in the codomain
    for pair in relation:
        domain.add(pair[0])
        codomain.add(pair[1])

    # If domain size = pairs, it's a function
    return len(domain) == len(relation)

def is_injective(relation):
    '''
    Injective Checker

    Inputs:
        list

    Ouputs:
        boolean value
    '''
    
    # init var (set)
    codomain_elements = set()

    # For all elements in codomain, are they assigned to no more than one element
    for pair in relation:
        codomain_elements.add(pair[1])

    # If codomain size = pairs, it's injective
    return len(codomain_elements) == len(relation)

def is_surjective(relation, codomain):
    '''
    Surjective Checker

    Inputs:
        2 lists

    Ouputs:
        boolean value
    '''

    # init var (set)
    relation_codomain_elements = set()

    # Is the codomain covered by the function for all elements?
    for pair in relation:
        relation_codomain_elements.add(pair[1])

    # If it is, it's surjective
    return relation_codomain_elements == set(codomain)

def is_bijective(relation, codomain):
    '''
    Bijective Checker

    Inputs:
        2 lists

    Outputs:
        boolean value
    '''

    # If something is a function, injective, and surjective, then it's bijective
    return is_function(relation) and is_injective(relation) and is_surjective(relation, codomain)

def inverse_function(relation):
    '''
    Inverse Finder

    Inputs:
        list

    Outputs:
        list
    '''
    # This swaps the tuples indexes like (a, b) -> (b, a)
    inverse = {(pair[1], pair[0]) for pair in relation}
    return inverse

def print_relation(relation, domain, codomain):
    '''
    Prints relation, domain, and codomain.

    Inputs:
        3 lists
        
    Outputs:
        n/a
    '''
    print(f"\tA = {set(domain)}")
    print(f"\tB = {set(codomain)}")
    print(f"\tf = {set(relation)}")

# Init list of relations
relations = [
    {"A": ["a", "b", "c", "d"], "B": ["v", "w", "x", "y", "z"], "f": [("a", "z"), ("b", "y"), ("c", "x"), ("d", "w")]},
    {"A": ["a", "b", "c", "d"], "B": ["x", "y", "z"], "f": [("a", "z"), ("b", "y"), ("c", "x"), ("d", "z")]},
    {"A": ["a", "b", "c", "d"], "B": ["w","x", "y", "z"], "f": [("a", "z"), ("b", "y"), ("c", "x"), ("d", "w")]},
    {"A": ["a", "b", "c", "d"], "B": [1, 2, 3, 4, 5], "f": [("a", 4), ("b", 5), ("c", 1), ("d", 3)]},
    {"A": ["a", "b", "c"], "B": [1, 2, 3, 4], "f": [("a", 3), ("b", 4), ("c", 1)]},
    {"A": ["a", "b", "c", "d"], "B": [1, 2, 3], "f": [("a", 2), ("b", 1), ("c", 3), ("d", 2)]},
    {"A": ["a", "b", "c", "d"], "B": [1, 2, 3, 4], "f": [("a", 4), ("b", 1), ("c", 3), ("d", 2)]},
    {"A": ["a", "b", "c", "d"], "B": [1, 2, 3, 4], "f": [("a", 2), ("b", 1), ("c", 2), ("d", 3)]},
    {"A": ["a", "b", "c"], "B": [1, 2, 3, 4], "f": [("a", 2), ("b", 1), ("a", 4), ("d", 3)]}
]

# Loop that iterates through the relations list so that it works through the functions for every relation
for i, relation_data in enumerate(relations, start=1):
    A = relation_data["A"]
    B = relation_data["B"]
    f = relation_data["f"]

    print(f"{i}:\n")
    print_relation(f, A, B)
    if is_function(f):
        print("\n\tThis relation is a function.")
        if is_bijective(f, B):
            print("\tIt is bijective.")
            print("\n\tThe inverse function is:\n")
            print_relation(inverse_function(f), B, A)
        else:
            if is_injective(f):
                print("\tIt is injective.")
            
            if is_surjective(f, B):
                print("\tIt is surjective.")
        
    else:
        print("\n\tThis relation is not a function.")

    print()

print('-------------------PROGRAM 2-------------------')

def euclidean_gcd(d, a, b):
    """
    Does the gcd and prints the steps

    Inputs:
        1 str, 2 int

    Outputs:
        int
    """
    
    # Prints the problem it is
    print(f'{d}.')

    # Calculates the gcd by looping until the remainder is 0 and pritns every step
    while b:
        q, r = divmod(a, b)
        print(f"\t{a}/{b} = {q} R {r}")
        a, b = b, r

    return a

def printegcd(d, a, b):
    """
    Prints the gcd in the format I want

    Inputs:
        1 str, 2 int
    """
    result = euclidean_gcd(d, a, b)
    print(f"\n\tgcd({a}, {b}) = {result}\n")

printegcd('1', 414, 662)
printegcd('2', 6, 14)
printegcd('3', 24, 36)
printegcd('4', 12, 42)
printegcd('5', 252, 198)

print('-------------------PROGRAM 3-------------------')

def extended_gcd(a, b):
    """
    Does the gcd and shows the steps of the extended euclidean algorithm

    Inputs:
        2 int

    Outputs:
        tuple
    """

    # init vars
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    forward_steps = []  
    backward_steps = []  

    # Loops while the remainder isn't 0 and calculates the gcd
    while r != 0:
        quotient = old_r // r
        forward_steps.append((old_r, r, quotient))
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # init gcd and bezouts coeefficients
    gcd = old_r
    coefficients = (old_s, old_t)
    
    # pritns all the forward steps
    print("\n\tForward steps:\n")
    for a, b, q in forward_steps:
        print(f"\t{a} = {b} * {q} + {a - b * q}")

    # printsall the backward steps
    print("\n\tBackward steps:\n")
    for i, (a, b, q) in enumerate(forward_steps):
        if i < len(forward_steps) - 1:
            next_a, next_b, next_q = forward_steps[i + 1]
            print(f"\t{a} = {b} - {q} * {next_a}")
        else:
            print(f"\t{a} = {s} * {a} + {t} * {b}")

    return gcd, coefficients

# init inputs
inputs = [
    (414, 662),
    (6, 14),
    (24, 36),
    (12, 42),
    (252, 198)
]

# Loop that iterates through the relations list so that it works through the extended gcd function for all my inputs
for i, (a, b) in enumerate(inputs, 1):
    print(f"{i}. gcd({a}, {b})")
    gcd, (s, t) = extended_gcd(a, b)
    print(f"\tgcd({a}, {b}) = {gcd} = {s}*{a} + {t}*{b}\n")

print('-------------------PROGRAM 4-------------------')

def extended_euclidean_gcd(a, b):
    """
    Does the gcd(a, b) using the extended Euclidean algorithm, and finds the bezout coefficients s and t

    Inputs:
        2 int

    Ouputs:
        n/a
    """

    # init var
    a0, b0 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    q_values = []

    # break if b is 0 and adds to a list of q values
    while b != 0:
        quotient = a // b
        q_values.append(quotient)

        a, b = b, a % b
        s0, s1 = s1, s0 - quotient * s1
        t0, t1 = t1, t0 - quotient * t1

    gcd = a
    s = s0
    t = t0

    # string comprehension for quotients
    print("\n\tQuotients (q values):", end=' ')
    for i, q in enumerate(q_values):
        print(f"q{i + 1} = {q}", end=', ' if i < len(q_values) - 1 else '\n')

    # s Values
    print("\n\tCalculations for s values:\n")
    for i in range(len(q_values)):
        print(f"\ts{i} = {1 if i == 0 else 0} - {1 if i == 1 else 0} * {q_values[i]} = {s0 if i == 0 else 0 - q_values[i] * s1}")

    # t values
    print("\n\tCalculations for t values:\n")
    for i in range(len(q_values)):
        print(f"\tt{i} = {0 if i == 0 else 1} - {0 if i == 1 else 1} * {q_values[i]} = {t0 if i == 0 else 1 - q_values[i] * t1}")

    # gcd expressed with bezout's coefficients
    print(f"\n\tgcd({a0}, {b0}) = {gcd} = {s}*{a0} + {t}*{b0}")

# init inputs
inputs = [
    (414, 662),
    (6, 14),
    (24, 36),
    (12, 42),
    (252, 198)
]

# loops through inputs and uses function to do the problem
for i, (a, b) in enumerate(inputs, 1):
    print(f"{i}. gcd({a}, {b})")
    extended_euclidean_gcd(a, b)
    print()





