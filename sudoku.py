import numpy as np
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


print("SUDOKU PUZZLE")
print(np.matrix(sudoku))

def cek(y,x,n):
    global sudoku
    
    #cek baris
    for i in range(0,9):
        if (sudoku[y][i]) == n :
            return False
    
    # cek kolom
    for i in range(0,9):
        if (sudoku[i][x]) == n :
            return False
    
    # cek kotak 3x3
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if (sudoku[y0+i][x0+j]) == n :
                return False
    return True

def selesai():
    global sudoku
    for y in range(9):
        for x in range(9):
            if (sudoku[y][x]) == 0 :
                for n in range(1,10):
                    if(cek(y,x,n)):
                        sudoku[y][x] = n
                        selesai()
                        sudoku[y][x] = 0
                return
    print(np.matrix(sudoku))


print("SUDOKU SOLUTION")
selesai()