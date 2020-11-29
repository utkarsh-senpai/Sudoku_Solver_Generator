import random
from random import sample
import sys
base = 3
side = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): return sample(s,len(s)) 

def ran(gen,k):
    squares = side*side
    empties = squares * 3//(9-k)
    for p in sample(range(squares),empties):
        gen[p//side][p%side] = 0
    #numSize = len(str(side))   

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(board,fstr):
    with open(fstr,"w") as fp:
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")
                fp.write("- - - - - - - - - - - - - \n")
            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                    fp.write(" | ")
                if j == 8:
                    print(board[i][j])
                    fp.write(str(board[i][j]))
                    fp.write("\n")
                else:
                    print(str(board[i][j]) + " ", end="")
                    fp.write("{box} ".format(box = board[i][j]))

#Used to find empty position or 0 in Sudoku grid.
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row,col

    return None

l = input("Enter 1 for Generating Sudoku \nEnter 2 for Solving Sudoku\nEnter Choice:\t")
try:
    l = int(l)
except:
    print("Enter Valid Entry")
    sys.exit()

#For Generating Sudoku
if l == 1:
    k = input("\nEnter Difficulty of Sudoku:\n1 for Easy\n2 for Medium\n3 for Hard\nEnter Number:\t")
    try:
        k = int(k)
    except:
        print("Enter Valid Entry")
        sys.exit()
    
    print("")
    rBase = range(base) 
    rows = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    gen_sudo = [[nums[pattern(r,c)] for c in cols] for r in rows]
    sol_sudo = nums
    #Function to remove spaces from sudoku
    ran(gen_sudo,k)
    print_board(gen_sudo,'generated_sudoku.txt')

    s = input("\nEnter 1 for Solution\t")
    try:
        l = int(l)
    except:
        print("Enter Valid Entry")
        sys.exit()
    solve(gen_sudo)
    print("")
    print_board(gen_sudo,'generated_sudoku_soln.txt')
    print("")


#For Solving Sudoku
elif l == 2:
    board = []
    try:
        with open('input_sudoku.txt',"r") as INPUT:
            sen = INPUT.readlines()
            for lines in sen:
                board.append(list(map(int,lines.split(","))))
        print("\nInput Sudoku Grid")
        print_board(board,'output_sudoku.txt')
        solve(board)
        print("\n\nSolved Sudoku Grid")
        print_board(board,'output_sudoku.txt')
        print("")
    except:
        print("Invalid Input File")

else:
    print("Enter Valid Entry")
    sys.exit()