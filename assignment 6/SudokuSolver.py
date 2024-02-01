'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
EECS210 Assignment 6
Description:
A program written to solve sudoku puzzles
Collaborators: None
Sources: None
Full Name: Tuan Vu
Creation Date: 11/09/2023
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def parse_puzzle_file(file_name):
    '''
    Parse Puzzle File

    Inputs:
        file

    Ouputs:
        list of strings
    '''
    # Opens file and reads file
    with open(file_name, "r") as file:
        # Initializes a list of strings, "lines", that reads the files lines into the variables getting rid of all whitespace and spaces 
        lines = file.read().replace(' ','').strip().splitlines()
    return lines

def formatlines(lines):
    '''
    Line Formatter (switches all strings to integers)

    Inputs:
        list of strings

    Ouputs:
        list of lists of integers
    '''
    # Initializes a list, "puzzle"
    puzzle = []
    # Iterates for every string, "line", in a list of strings, "lines"
    for line in lines:
        # Initializes a list, "puzzleline"
        puzzleline = []
        # Iterates for every character in every string, "line"
        for char in line:
            # If the character is not "_", then it will append the integer to the list, "puzzleline"
            if char != '_':
                puzzleline.append(int(char))
            # Else the character is a "_", then it will append the 0 to the list, "puzzleline"
            else:
                puzzleline.append(0)
        # Appends the list, "puzzleline", to the list, "puzzle".
        # Effectively creating a list of lists
        puzzle.append(puzzleline)
    return puzzle

def print_grid(grid):
    '''
    Grid Printer

    Inputs:
        list of lists of integers

    Ouputs:
        n/a (it does print the input in a grid format like sudoku)
    '''
    # Iterates for every list of integers in a list of lists, "grid"
    for row in grid:
        # Prints every list of integers turning each row into a string where every character is joined by spaces
        # Prints a nicely formatted sudoku grid 
        print(" ".join(map(str, row)))

def is_valid_move(grid, row, col, num):
    '''
    Valid Move Checker 

    Inputs:
        list of lists of integers
        integer
        integer
        integer

    Ouputs:
        boolean
    '''
    # If the integer, "num", is in the list, "row", or the list, "column", returns false
    if num in grid[row] or num in [grid[i][col] for i in range(9)]:
        return False

    # Algorithm to calculate the start of each 3x3 block
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    # If the integer, "num", is in the 3x3 block, returns False
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    '''
    Sudoku Solver

    Inputs:
        list of lists of integers

    Ouputs:
        boolean
    '''
    # Iterates through each cell (3x3 block)
    for row in range(9):
        for col in range(9):
            # If the cell is empty
            if grid[row][col] == 0:
                # Iterates through the range of possible numbers in sudoku
                for num in range(1, 10):
                    # Checks if putting a number in a cell is valid
                    if is_valid_move(grid, row, col, num):
                        # Puts the number in the cell if it is valid
                        grid[row][col] = num
                        # Updates the sudoku grid
                        if solve_sudoku(grid):
                            return True
                        # Backtracks if no solution is found
                        grid[row][col] = 0
                # Returns false if there's no valid numbers for the curent cell
                return False
    # Returns True when the grid is filled
    return True

def main():
    '''
    Driver function

    Inputs:
        n/a

    Ouputs:
        n/a
    '''
    # Initialize list of test cases
    puzzle_files = ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt", "puzzle4.txt", "puzzle5.txt"]

    # Iterates through the list of test cases, "puzzle_files"
    for file_name in puzzle_files:
        print("\n\nPuzzle:", file_name)
        # Reads file into variable, "puzzle"
        puzzle = parse_puzzle_file(file_name)

        print("Original Puzzle:")
        # Prints original puzzle
        print_grid(puzzle)
        
        # Converts puzzle into list of lists of integers
        puzzle = formatlines(puzzle)
        
        # Solves the puzzle
        if solve_sudoku(puzzle):
            print("\nSolution:")
            # Prints the puzzle that is solved
            print_grid(puzzle)
        else:
            print("\nNo solution found")

if __name__ == "__main__":
    main()
