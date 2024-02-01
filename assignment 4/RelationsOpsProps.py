

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
EECS210 Assignment 4
Description:
A program written in python for demonstrating operations on relations and properties of relations
Collaborators: None
Sources: ChatGPT
Full Name: Tuan Vu
Creation Date: 10/12/2023
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''
1. Reflexive code
'''''''''''''''''''''

#####################
# Define functions  #
#####################

def is_reflexive(relation, set):
    
    # Inputs: a relation, a set
    # Outputs: Boolean values
    
    for ele in set:
        # For every element in the set, if (ele, ele) does not exist within the relation it will return False because it's not reflexive
        if (ele, ele) not in relation:
            return False
    # Otherwise it is True
    return True

def find_reflexive_closure(relation, set):
    
    # Inputs: a relation, a set
    # Outputs: the reflexive closure of input relation
    
    # Define new relation closure as a copy of the relation
    closure = relation.copy()
    for ele in set:
        # For every element in the set, if (ele, ele) does not exist within the closure relation then it will append it into the closure relation
        if (ele, ele) not in closure:
            closure.append((ele, ele))
    return closure

def ref_output(relation, set):
    
    # Inputs: a relation, a set
    # Outputs: well formatted print of the answer
    
    # Handles formatted print statement for examples
    print("\t\ta) R =", relation)
    print("\t\tb) R is reflexive:", is_reflexive(relation, set))
    # If it's not reflexive it will also print it's reflexive closure
    if not is_reflexive(relation, set):
        print("\t\tc) R* if not reflexive:", find_reflexive_closure(relation, set))

#####################
# Examples          #
#####################

# Example 1
print("1.\tEx 1:")
relation1 = [(1, 1), (4, 4), (2, 2), (3, 3)]
set1 = {1, 2, 3, 4}
ref_output(relation1, set1)

# Example 2
print("\tEx 2:")
relation2 = [('a','a'), ('c','c')]
set2 = {'a', 'b', 'c', 'd'}
ref_output(relation2, set2)
print()


'''''''''''''''''''''
2. Symmetric code
'''''''''''''''''''''

#####################
# Define functions  #
#####################

def is_symmetric(relation):

    # Inputs: a relation
    # Outputs: Boolean value
    
    for (a, b) in relation:
        # For every set (a, b) in the relation, if (b, a) does not exist within the relation it will return False because it's not symmetric
        if (b, a) not in relation:
            return False
    # Otherwise it is True
    return True

def find_symmetric_closure(relation):
    
    # Inputs: a relation
    # Outputs: the symmetric closure of the input relation

    # Define new relation closure as a copy of the relation 
    closure = relation.copy()
    for (a, b) in relation:
        # For every set (a, b) in the relation, if (b, a) does not exist within the closure relation then it will append it into the closure relation
        if (b, a) not in closure:
            closure.append((b, a))
    return closure

def sym_output(relation):
    
    # Inputs: a relation, a set
    # Outputs: well formatted print of the answer
    
    # Handles formatted print statement for examples
    print("\t\ta) R =", relation)
    print("\t\tb) R is symmetric:", is_symmetric(relation))
    # If it's not symmetric it will also print it's symmetric closure
    if not is_symmetric(relation):
        print("\t\tc) R* if not symmetric:", find_symmetric_closure(relation))

#####################
# Examples          #
#####################
        
# Example 1:
print("2.\tEx 1:")
relation1 = [(1, 2), (4, 4), (2, 1), (3, 3)]
sym_output(relation1)

# Example 2:
print("\tEx 2:")
relation2 = [(1, 2), (3, 3)]
sym_output(relation2)
print()


'''''''''''''''''''''
3. Transitive Code
'''''''''''''''''''''

#####################
# Define functions  #
#####################

def is_transitive(relation, set):
    
    # Inputs: a relation, a set
    # Outputs: Boolean value
    
    for a in set:
        for b in set:
            for c in set:
                # For a, b, and c in the set, if (a, b), (b, c), and (a, c) does not exist within the relation it will return False because it's not transitive
                if ((a, b) in relation and (b, c) in relation) and (a, c) not in relation:
                    return False
    # Otherwise it is True
    return True

def find_transitive_closure(relation, set):
        
    # Inputs: a relationm, a set
    # Outputs: the transitive closure of the input relation

    # Define new relation closure as a copy of the relation 
    transitive_closure = relation.copy()
    for a in set:
        for b in set:
            for c in set:
                # For a, b, and c in the set, if (a, b), (b, c), and (a, c) does not exist within the relation it will append (a, c) into the closure
                if ((a, b) in transitive_closure and (b, c) in transitive_closure) and (a, c) not in transitive_closure:
                    transitive_closure.append((a, c))
    return transitive_closure

def tran_output(relation, set):
        
    # Inputs: a relation, a set
    # Outputs: well formatted print of the answer
    
    # Handles formatted print statement for examples
    print("\t\ta) R =", relation)
    print("\t\tb) R is transitive:", is_transitive(relation, set))
    # If it's not transitive it will also print it's transitive closure
    if not is_transitive(relation, set):
        print("\t\tc) R* if not transitive:", find_transitive_closure(relation, set))

#####################
# Examples          #
#####################

# Example 1:
print("3.\tEx 1:")
relation1 = [('a','b'), ('d','d'), ('b','c'), ('a','c')]
set1 = {'a', 'b', 'c', 'd'}
tran_output(relation1, set1)

# Example 2:
print("\tEx 2:")
relation2 = [(1, 1), (1, 3), (2, 2), (3, 1), (3, 2)]
set2 = {1, 2, 3}
tran_output(relation2, set2)


'''''''''''''''''''''
4. Equivalence relation code
'''''''''''''''''''''

#####################
# Define functions  #
#####################

def eq_output(relation, set):
        
    # Inputs: a relation, a set
    # Outputs:  a well formatted print of the answer with reasons

    # Handles formatted print statement for examples
    print("\t\ta) R =", relation)
    # Equivalence relation means that it is reflexive, symmetric, and transitive
    if is_reflexive(relation, set) and is_symmetric(relation) and is_transitive(relation, set):
        # If the relation is reflexive, symmetric, and transitive, state that it is an equivalence relation
        print("\t\tb) R is an equivalence relation")
    else:
        # If the relation isn't reflexive, symmetric, and/or transitive, state that it is not an equivalence relation
        print("\t\tb) R is not an equivalence relation")
        if not is_reflexive(relation, set):
            # If relation isn't reflexive, state it is not reflexive
            print("\t\tc) R is not reflexive.")
        if not is_symmetric(relation):
            # If relation isn't symmetric, state it is not symmetric
            print("\t\tc) R is not symmetric.")
        if not is_transitive(relation, set):
            # If relation isn't transitive, state it is not transitive
            print("\t\tc) R is not transitive.")

#####################
# Examples          #
#####################

# Example 1:
print("4.\tEx 1:")
relation1 = [(1, 1), (2, 2), (2, 3)]
set1 = {1, 2, 3}
eq_output(relation1, set1)

# Example 2:
print("\tEx 2:")
relation2 = [('a', 'a'), ('b', 'b'), ('c', 'c'), ('b','c'), ('c','b')]
set2 = {'a', 'b', 'c'}
eq_output(relation2, set2)
print()


'''''''''''''''''''''
5. Is a poset? code
'''''''''''''''''''''

#####################
# Define functions  #
#####################

def is_antisymmetric(relation):
        
    # Inputs: a relation
    # Outputs: Boolean value
    
    for (a, b) in relation:
        # For set (a, b) in the relation, if a doesn't equal b and (b, a) is in the relation does not exist within the relation it will return False because it's not antisymmetric
        if a != b and ((b, a) in relation):
            return False
    # Otherwise it's True
    return True

def p_output(relation, set):
            
    # Inputs: a relation, a set
    # Outputs:  a well formatted print of the answer with reasons

    # Handles formatted print statement for examples
    print("\t\ta) S =", set)
    print("\t\tb) R =", relation)
    # A relation is a poset if it is reflexive, antisymmetric, and transitive
    if is_reflexive(relation, set) and is_antisymmetric(relation) and is_transitive(relation, set):
        # If the relation is reflexive, antisymmetric, and transitive, state that it is a poset
        print("\t\tc) (S, R) is a poset:", True)
    else:
        # If the relation is not reflexive, antisymmetric, and/or transitive, state it is not a poset
        print("\t\tc) (S, R) is a poset:", False)
        if not is_reflexive(relation, set):
            # If the relation isn't reflexive, state it is not reflexive
            print("\t\td) (S, R) isn't a poset because it is not reflexive")
        if not is_antisymmetric(relation):
            # If the relation isn't antisymmetric, state it is not antisymmetric
            print("\t\td) (S, R) isn't a poset because it is not antisymmetric")
        if not is_transitive(relation, set):
            # If the relation isn't transitive, state it is not transitive
            print("\t\td) (S, R) isn't a poset because it is not transitive")

#####################
# Examples          #
#####################

# Example 1:
print("5.\tEx 1:")
relation1 = [(1,1),(1,2),(2,2),(3,3),(4,1),(4,2),(4,4)]
set1 = {1, 2, 3, 4}
p_output(relation1, set1)

# Example 2:
print("\tEx 2:")
relation2 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)]
set2 = {0, 1, 2, 3}
p_output(relation2, set2)

