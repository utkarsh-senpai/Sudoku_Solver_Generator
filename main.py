import random
from random import sample
import sys
base  = 3
side  = base*base
# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)

def shuffle(s): return sample(s,len(s)) 
def ran(gen,k):
    squares = side*side
    empties = squares * 3//(9-k)
    # print("Empties = {emp}".format(emp = empties))
    for p in sample(range(squares),empties):
        gen[p//side][p%side] = 0

    numSize = len(str(side))   

def solve(bo): #solving Sudoku Backtracking
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos): #Checking row, column and box.
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):#Used for priting board.
    with open('output1.txt',"w") as fp:
        for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")
                fp.write("- - - - - - - - - - - - - \n")
            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                    fp.write(" | ")
                if j == 8:
                    print(bo[i][j])
                    fp.write(str(bo[i][j]))
                    fp.write("\n")
                else:
                    print(str(bo[i][j]) + " ", end="")
                    fp.write("{box} ".format(box = bo[i][j]))

def find_empty(bo):#Used to find empty position or 0 in Sudoku grid.
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

l = input("Enter 1 for Generating Sudoku. \n2 for solving Sudoku in text file 'input.txt':\t")
l = int(l)
if l == 1:#FOr Generating Sudoku
    k = input("Enter Difficulty of Sudoku:\n1 for easy\n2 for medium\n3 for hard\nEnter Number:\t")
    k= int(k)
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    gen = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    ran(gen,k) ##Function to remove spaces from sudoku
    with open("output2.txt","w") as inp:
        for line in gen:
            for i in range(len(line)):
                if i!=(len(line)-1):
                    print(line[i], end=",")
                    inp.write("{i},".format(i=line[i]))
                else:
                    print(line[i])
                    inp.write(str(line[i]))
                    inp.write("\n")
elif l == 2:#For taking input from input.txt and output in output.txt
    board = []

    with open('input.txt',"r") as INPUT:
        sen = INPUT.readlines()
        for lines in sen:
            board.append(list(map(int,lines.split(","))))
    print("Input Sudoku Grid.")
    print_board(board)
    solve(board)
    print("_______________________________________________")
    print("Solved Sudoku Grid.")
    print_board(board)
else:
    print("Enter valid entries.")
    sys.exit()