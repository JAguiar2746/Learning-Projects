from pprint import pprint

def find_next_empty(puzzle):
    #finds the next row,col on the puzzle that is empty
    #returns row, col tuple 

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    
    return None,None

def is_valid(puzzle,guess,row,col):
    #check if the guess number is already in the puzzle row 
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    #check the columns now
    col_vals= [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #check the 3x3 box
    row_start = (row//3) * 3
    col_start = (col//3) * 3

    for r in range(row_start, row_start +3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True



def solve_sudoku(puzzle):
    #solves sudoku using backtracking

    #step 1: find a spot to start
    row,col = find_next_empty(puzzle)
    #if there is now where left then we are done with the puzzle
    if row is None:
        return True
    
    #step 2: if there is an available spot make a guess between 1 and 9
    for guess in range(1,10):
        #step 3: check if the guess is a valid guess in respect to the row, column, and matrix of the current spot
        if is_valid(puzzle, guess, row, col):
            #if the guess was valid then place that guess on the puzzle
            puzzle[row][col] = guess            
            #step 4: now we recursively call our function
            if solve_sudoku(puzzle):
                return True
        #step 5: if not valid or if our guess does not solve the puzzle then we need to backtrack and try a new puzzle
        puzzle[row][col] = -1 # reset the spot

    #step 6: if none of our previous attemps work the the puzzle is unsolveable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
