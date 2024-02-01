'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
EECS210 Assignment 7
Description:
A program for the four different type of counting having to do with distinguishable and indistinguishable boxes and objects.
Collaborators: None
Sources: None
Full Name: Tuan Vu
Creation Date: 11/28/2023
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from math import factorial

def c_no_rep(n, k):
    # Combinations without repetition
    # Inputs:
    #     n: number of objects
    #     k: number of boxes
    # Outputs:
    #     result: number of combinations without repetition
    return factorial(n) // (factorial(k) * factorial(n - k))

def dd(objects, amt, boxes):
    # Distinguishable objects into distinguishable boxes
    # Inputs:
    #     objects: number of objects
    #     amt: number of objects per box
    #     boxes: number of boxes
    # Outputs:
    #     result: number of combinations
    result = 1 # Initialize var to represent the result
    while amt > 0: # Iterate through the range of amt
        result *= c_no_rep(objects, boxes) # Multiply the result by the number of combinations without repetition
        objects -= boxes # Subtract boxes from objects
        amt -= 1 # Decrement amt
    return result

def id(objects, boxes):
    # Indistinguishable objects into distinguishable boxes
    # Inputs:
    #     objects: number of objects
    #     boxes: number of boxes
    # Outputs:
    #     result: number of combinations
    return c_no_rep(objects + boxes - 1, objects)

def stirling_second(n, j):
    # Stirling numbers of the second kind
    # Inputs:
    #     n: number of objects
    #     j: number of boxes
    # Outputs:
    #     result: number of combinations
    summation = 0 # Initialize var to represent summation of the terms
    for i in range(0, j): # Iterate through the range of i from 0 to j
        summation += c_no_rep(j,i)*((j-i)**n)*((-1)**i) # Add the term to the summation
    result = summation//factorial(j) # Divide the summation by j factorial
    return result
        
def di(n, k):
    term = 0 # Initialize var to represent the term
    for j in range(1, k + 1): # Iterate through the range of j from 1 to k + 1
        term += stirling_second(n, j) # Add the term to the jth Stirling number of the second kind
    return term # Return the term
    
def pk(n, k): 
    if n == 0 and k == 0: # Base case if n and k are both 0
        return 1
    if (n <= 0 or k <= 0): # Base case if n or k are less than or equal to 0
        return 0
    return pk(n - k, k) + pk(n - 1, k - 1) # Return the sum of the two recursive calls

def ii(n, k):
    term = 0 # Initialize var to represent the term
    for j in range(1, k + 1): # Iterate through the range of j from 1 to k + 1
        term += pk(n, j) # Add the term to the jth partition number
    return term

# Problem 1
print("1.")

result_a = dd(52, 4, 5)
print("\ta)\n\t\tResult:", result_a)
result_b = dd(40, 4, 10)
print("\tb)\n\t\tResult:", result_b, "\n")

# Problem 2
print("2.")

result_a = id(10, 8)
print("\ta)\n\t\tResult:", result_a)
result_b = id(12, 6)
print("\tb)\n\t\tResult:", result_b, "\n")

# Problem 3
print("3.")

result_a = di(4, 3)
print("\ta)\n\t\tResult:", result_a)
result_b = di(5, 4)
print("\tb)\n\t\tResult:", result_b, "\n")

# Problem 4
print("4.")

result_a = ii(6, 4)
print("\ta)\n\t\tResult:", result_a)
result_b = ii(5, 3)
print("\tb)\n\t\tResult:", result_b, "\n")
