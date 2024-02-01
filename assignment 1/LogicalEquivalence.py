'''
Tuan Vu

8/31/2023

EECS 210 Assignment 1

Description: prints out truth tables showing the logical equivalence of the propositions given.
'''

# Demorgan's First Law
def demorgans1():
    # The title of the truth table
    print("1. De Morgan's First Law")
    # The format of table and how much work I want to show
    print("P\t\tQ\t\t¬P\t\t¬Q\t\tP ∧ Q\t\t¬(P ∧ Q)\t\t¬P ∨ ¬Q")
    # Iterate through True and False with P and Q variable
    for p in [True, False]:
        for q in [True, False]:
            # Stores results of Boolean propositions to make code more organized
            result0 = p and q
            result1 = not (p and q)
            result2 = not p or not q
            # Prints results step by step in a format that correlates with the format of table
            print(f"{p}\t\t{q}\t\t{not p}\t\t{not q}\t\t{result0}\t\t{result1}\t\t{result2}")
    # Prints new line for formatting
    print()

# Demorgan's Second Law
def demorgans2():
    # The title of the truth table
    print("2. De Morgan's Second Law")
    # The format of table and how much work I want to show
    print("P\t\tQ\t\t¬P\t\t¬Q\t\tP ∨ Q\t\t¬(P ∨ Q)\t\t¬P ∧ ¬Q")
    # Iterate through True and False with P and Q variable
    for p in [True, False]:
        for q in [True, False]:
            # Stores results of Boolean propositions to make code more organized
            result0 = p or q
            result1 = not (p or q)
            result2 = not p and not q
            # Prints results step by step in a format that correlates with the format of table
            print(f"{p}\t\t{q}\t\t{not p}\t\t{not q}\t\t{result0}\t\t{result1}\t\t{result2}")
    # Prints new line for formatting
    print()

# First Associative Law
def asso_law1():
    # The title of the truth table
    print("3. First Associative Law")
    # The format of table and how much work I want to show
    print("P\t\tQ\t\tR\t\tP ∧ Q\t\t(P ∧ Q) ∧ R\tP ∧ (Q ∧ R)")
    # Iterate through True and False with P , Q, and R variable
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                # Stores results of Boolean propositions to make code more organized
                result0 = p and q
                result1 = result0 and r
                result2 = p and (q and r)
                # Prints results step by step in a format that correlates with the format of table
                print(f"{p}\t\t{q}\t\t{r}\t\t{result0}\t\t{result1}\t\t{result2}")
    # Prints new line for formatting
    print()

# Second Associative Law
def asso_law2():
    # The title of the truth table
    print("4. Second Associative Law")
    # The format of table and how much work I want to show
    print("P\t\tQ\t\tR\t\tP ∨ Q\t\t(P ∨ Q) ∨ R\tP ∨ (Q ∨ R)")
    # Iterate through True and False with P, Q, and R variable
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                # Stores results of Boolean propositions to make code more organized
                result0 = p or q
                result1 = result0 or r
                result2 = p or (q or r)
                # Prints results step by step in a format that correlates with the format of table
                print(f"{p}\t\t{q}\t\t{r}\t\t{result0}\t\t{result1}\t\t{result2}")           
    # Prints new line for formatting
    print()

# [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T
def func1():
    # The title of the truth table
    print("5. [(P ∨ Q) ∧ (P → R) ∧ (Q → R)] → R ≡ T")
    # The format of table and how much work I want to show
    print("P\t\tQ\t\tR\t\tP ∨ Q\t\tP → Q\t\tQ → R\t\t[(P ∨ Q) ∧ (P → R) ∧ (Q → R)] → R")
    # Iterate through True and False with P, Q, and R variable
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                # Stores results of Boolean propositions to make code more organized
                result0 = p or q
                result1 = (not p) or q
                result2 = (not q) or r
                result3 = result0 and result1 and result2
                result4 = not result3 or r
                # Prints results step by step in a format that correlates with the format of table
                print(f"{p}\t\t{q}\t\t{r}\t\t{result0}\t\t{result1}\t\t{result2}\t\t{result4}")           
    # Prints new line for formatting
    print()

# p ↔ q ≡ (p → q) ∧ (q → p)
def func2():
    # The title of the truth table
    print("6. P ↔ Q ≡ (P → Q) ∧ (Q → P)")
    # The format of table and how much work I want to show
    print("P\t\tQ\t\tP → Q\t\tQ → P\t\t(P → Q) ∧ (Q → P)\tP ↔ Q")
    # Iterate through True and False with P and Q variable
    for p in [True, False]:
        for q in [True, False]:
            # Stores results of Boolean propositions to make code more organized
            result0 = not p or q
            result1 = not q or p
            result2 = result0 and result1
            result3 = (p and q) or (not p and not q)
            # Prints results step by step in a format that correlates with the format of table
            print(f"{p}\t\t{q}\t\t{result0}\t\t{result1}\t\t{result2}\t\t{result3}")           
    # Prints new line for formatting
    print()

# Main function
def main():
    # Calling all of the functions (sort of redundant, but good practice to get into)
    demorgans1()
    demorgans2()
    asso_law1()
    asso_law2()
    func1()
    func2()

# Calling the main function
main()
    
