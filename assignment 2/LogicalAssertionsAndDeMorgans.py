# EECS 210 Assignment 3
# Python program to evaluate logical assertions and De Morgan's Law.
# Inputs: None
# Outputs: Results of logical assertions
# Collaborators: None
# Other sources for the code: None
# Author: Tuan Vu
# Creation date: 9-14-2023

# Define the domain
domain = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define the statements P(x), Q(x), R(x), notR(x)
def P(x):
    return x < 2

def Q(x):
    return x > 7


# Helper function to evaluate De Morgan's Law with Universal Quantifiers
def demorgans_law_U(domain):
    for x in domain:
        if x < 5:
            return True
    return False

# Helper function to evaluate De Morgan's Law with Existential Quantifiers
def demorgans_law_E(domain):
    for x in domain:
        if x < 5:
            return False
    return True

# Helper function to print the result
def print_result(statement, result, counterexample=None):
    print(f"{statement}: {result} \t (Example: {counterexample})")


# Question 1
print('1)')
# Check if there exists x such that P(x) is true and provide example
for x in domain:
    if P(x):
        example_x_1a = x
print_result("1a", any(P(x) for x in domain), example_x_1a)  # Should be True

# Check if for all x, P(x) is true and provide example
result_1b = all(P(x) for x in domain)
for x in domain:
    if not P(x):
        counterexample_x_1b = x
        break
print_result("1b", result_1b, counterexample_x_1b)

# Check if there exists x such that (P(x) or Q(x)) is true and provide an example
for x in domain:
    if P(x) or Q(x):
        example_x_1b = x
        break
print_result("1c", any(P(x) or Q(x) for x in domain), example_x_1b)

# Check if for all x, (P(x) or Q(x)) is true and provide an example
result_1d = all(P(x) or Q(x) for x in domain)
for x in domain:
    if not (P(x) or Q(x)):
        counterexample_x_1d = x
        break
print_result("1d", result_1d, counterexample_x_1d)

# Check De Morgan's Law for the Existential Quantifier and provide an example
if demorgans_law_E(domain):
    for x in domain:
        if x < 5:
            example_x_1e = x
            break
    print_result("1e", demorgans_law_E(domain), example_x_1e)
else:
    for x in domain:
        if not x < 5:
            counter_example_x_1e = x
            break
    print_result("1e", demorgans_law_E(domain), counter_example_x_1e)

# Check De Morgan's Law for the Universal Quantifier and provide an example
if demorgans_law_U(domain):
    for x in domain:
        if not x < 5:
            example_x_1e = x
            break
    print_result("1f", demorgans_law_U(domain), example_x_1e)
else:
    for x in domain:
        if x < 5:
            counter_example_x_1e = x
            break
    print_result("1f", demorgans_law_U(domain), counter_example_x_1e)

# Define the domain for x and y
domain_x = [1, 2, 4, 5, 10, 0.5, 0.25, 0.2, 0.1]
domain_y = domain_x

# Define the statement P(x, y)
def P(x, y):
    return x * y == 1

# Question 2
print()
print('2)')
# Check if for all x and y, P(x, y) is true and provide an example
result_2a = all(all(P(x, y) for x in domain_x) for y in domain_y)

if result_2a:
    tdict_2a = {}
    for x in domain_x:
        for y in domain_y:
            if P(x,y):
                tdict_2a[y]=x
    tdata2a = ''.join([f'({x},{y})' for x,y in tdict_2a.items()])
    print_result("2a", True, tdata2a)
else:
    fdict_2a = {}
    for x in domain_x:
        for y in domain_y:
            if not P(x,y):
                fdict_2a[y]=x
    fdata2a = ''.join([f'({x},{y})' for x,y in fdict_2a.items()])
    print_result("2a", False, fdata2a)
    
# Check if for all x, there exists y such that P(x, y) is true and provide an example
result_2b = all(any(P(x, y) for y in domain_y) for x in domain_x)

if result_2b:
    tdict_2b = {}
    for x in domain_x:
        for y in domain_y:
            if P(x,y):
                tdict_2b[y]=x
    tdata2b = ''.join([f'({x},{y}), ' for x,y in tdict_2b.items()])
    print_result("2b", True, tdata2b)
else:
    fdict_2b = {}
    for x in domain_x:
        for y in domain_y:
            if not P(x,y):
                fdict_2b[y]=x
    fdata2b = ''.join([f'({x},{y})' for x,y in fdict_2b.items()])
    print_result("2b", False, fdata2b)
    
    
# Check if for all y, there exists x such that P(x, y) is true
result_2c = all(any(P(x, y) for x in domain_x) for y in domain_y)

if result_2c:
    tdict_2c = {}
    for x in domain_x:
        for y in domain_y:
            if P(x,y):
                tdict_2c[y]=x
    tdata2c = ''.join([f'({x},{y}), ' for x,y in tdict_2c.items()])
    print_result("2c", True, tdata2c)
else:
    fdict_2c = {}
    for x in domain_x:
        for y in domain_y:
            if not P(x,y):
                fdict_2c[y]=x
    fdata2c = ''.join([f'({x},{y})' for x,y in fdict_2c.items()])
    print_result("2c", False, fdata2c)

# Check if there exists x such that for all y, P(x, y) is true
result_2d = any(all(P(x, y) for y in domain_y) for x in domain_x)
if result_2d:
    tdict_2d = {}
    for x in domain_x:
        for y in domain_y:
            if P(x,y):
                tdict_2d[x]=y
    tdata2d = ''.join([f'({y},{x}), ' for x,y in tdict_2d.items()])
    print_result("2d", True, tdata2d)
else:
    fdict_2d = {}
    for x in domain_x:
        for y in domain_y:
            if not P(x,y):
                fdict_2d[x]=y
    fdata2d = ''.join([f'({y},{x})' for x,y in fdict_2d.items()])
    print_result("2d", False, fdata2d)

# Check if there exists y such that for all x, P(x, y) is true
result_2e = any(all(P(x, y) for x in domain_x) for y in domain_y)
if result_2e:
    tdict_2e = {}
    for x in domain_x:
        for y in domain_y:
            if P(x,y):
                tdict_2e[x]=y
    tdata2e = ''.join([f'({x},{y}), ' for x,y in tdict_2e.items()])
    print_result("2e", True, tdata2e)
else:
    fdict_2e = {}
    for x in domain_x:
        for y in domain_y:
            if not P(y,x):
                fdict_2e[x]=y
    fdata2e = ''.join([f'({x},{y})' for x,y in fdict_2e.items()])
    print_result("2e", False, fdata2e)


# Check if there exists x and y such that P(x, y) is true
result_2f = any(any(P(x, y) for y in domain_y) for x in domain_x)
if result_2f:
    tdict_2f = {}
    for x in domain_x:
        for y in domain_y:
            if P(x,y):
                tdict_2f[x]=y
    tdata2f = ''.join([f'({x},{y}), ' for x,y in tdict_2f.items()])
    print_result("2f", True, tdata2f)
else:
    fdict_2e = {}
    for x in domain_x:
        for y in domain_y:
            if not P(y,x):
                fdict_2f[x]=y
    fdata2f = ''.join([f'({x},{y})' for x,y in fdict_2f.items()])
    print_result("2f", False, fdata2f)
