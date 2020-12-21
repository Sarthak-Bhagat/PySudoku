#Sudoku.py 

import random
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],  #2D-List
         [0, 0, 0, 0, 0, 0, 0, 0, 0], #stores Grid
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
         
sb = [[0 for i in range(9)] for j in range(9)]


def RemoveKSpaces(k,bo):
  while k>=0:
    row=random.randint(0,8)
    col=random.randint(0,8)
    if bo[row][col] != 0:
      bo[row][col]=0
      k=k-1
    

def FillGrid(bo):
  r=list(range(1,9))
  find = find_empty(bo)
  if not find:
    return True
  else:
    row,col=find
  random.shuffle(r)
  for i in range(9):
    if valid(bo, i, (row, col)):
      bo[row][col] = r[i]
      if solve(bo):
        return True
    bo[row][col] = 0

  return False

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
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



def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

def BuildGrid():
  FillGrid(grid)
  for i in range(9):
    for j in range(9):
      sb[i][j] = int(grid[i][j])
  k=20
  RemoveKSpaces(k,grid)
  return 

BuildGrid()