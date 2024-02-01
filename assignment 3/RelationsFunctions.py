# EECS 210 Assignment 3
# Description: Demonstrating union, intersection, difference, and composition on relations and properties of relations.

# Author: Tuan Vu
# Date: 9/28/23

# Initialize R1 and R2 sets
R1 = {(1, 1), (2, 2), (3, 3)}
R2 = {(1, 1), (1, 2), (1, 3), (1, 4)}

# Initialize R and S sets
R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}
S = {(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)}

# Function for composite using iteration on both input sets to create the composition set
# Inputs: R and S (two sets)
# Output: Composition of R and S
def composite(R, S):
    result = set()
    for a, c in R:
        for b, d in S:
            if c == b:
                result.add((a, d))
    return result

# Function for checking reflexive using iteration to check if is an (a,a) in the set
# Inputs: R
# Output: Boolean statement that tells whether R is reflexive or not
def is_reflexive(R):
    for (a,b) in R:
        if (a,a) not in R:
            return False
    return True

# Function for checking symmetry using iteration to check if for (a,b) there exists a (b,a) in the set
# Inputs: R
# Output: Boolean statement that tells whether R is symmetric or not
def is_symmetric(R):
    for (a,b) in R:
        if (b,a) not in R:
            return False
    return True

# Function for checking antisymmetry using iteration to check if for (a,b) there exists a (b,a) and a!=b because (1,1), (2,2), ... cannot be considered
# Inputs: R
# Output: Boolean statement that tells whether R is antisymmetric or not
def is_antisymmetric(R):
    for (a,b) in R:
        if (b,a) in R and a != b:
            return False
    return True

# Function for checking transitive using iteration to check if for (a,b) and (c,d) there exists b==c and an (a,d)
# Inputs: R
# Output: Boolean statement that tells whether R is transitive or not
def is_transitive(R):
    for (a,b) in R:
        for (c,d) in R:
            if b == c and (a,d) not in R:
                return False
    return True

# Function to build set for the relation R = {(x, y) | x + y = 0} on the set {-10, ..., -1, 0, 1, ..., 10} by iterating ranges from -10 to 11 and seeing if they are in the solution set of x+y=0 then adding it to the set
# Inputs:
# Output: Solution set for R = {(x, y) | x + y = 0} on the set {-10, ..., -1, 0, 1, ..., 10}
def setbuilder():
    Rset = set()
    for x in range(-10,11,1):
        for y in range(-10,11,1):
            if x + y == 0:
                Rset.add((x,y))
    return Rset

# Print and call the functions to perform operations and check properties.
Rset = setbuilder()
print("1a. Union of R1 and R2:", R1.union(R2))
print("1b. Intersection of R1 and R2:", R1.intersection(R2))
print("1c. R1 - R2:", R1.difference(R2))
print("1d. R2 - R1:", R2.difference(R1))
print("2. S ◦ R:", composite(R,S))
print("3. R^2:", composite(R,R))
print("4a. Show R as a set of ordered pairs", Rset)
print("4b. Is R reflexive?", is_reflexive(Rset))
print("4c. Is R symmetric?", is_symmetric(Rset))
print("4d. Is R antisymmetric?", is_antisymmetric(Rset))
print("4e. Is R transitive?", is_transitive(Rset))
