from sudoku import Sudoku

values1 = [7, 0, 0,     0, 0, 8,    0, 0, 1,
           0, 1, 0,     0, 0, 0,    0, 3, 0,
           0, 0, 0,     0, 0, 0,    0, 0, 0,

           0, 0, 0,     0, 0, 0,    0, 0, 7,
           0, 0, 0,     0, 1, 0,    0, 0, 0,
           5, 0, 0,     0, 0, 0,    0, 0, 0,

           0, 0, 0,     0, 0, 0,    0, 0, 0,
           0, 2, 0,     0, 0, 0,    0, 1, 0,
           1, 0, 0,     8, 0, 0,    0, 0, 4]


values2 = [ 9, 3, 0,    0, 5, 0,    0, 0, 0,
            0, 0, 0,    2, 0, 0,    0, 0, 5,
            0, 0, 0,    7, 1, 9,    0, 8, 0,

            0, 5, 0,    0, 8, 7,    0, 0, 0,
            2, 0, 6,    0, 0, 3,    0, 0, 0,
            0, 0, 0,    0, 0, 0,    0, 0, 4,

            5, 0, 0,    0, 0, 0,    0, 0, 0,
            6, 7, 0,    1, 0, 5,    0, 4, 0,
            1, 0, 9,    0, 0, 0,    2, 0, 0]

sudoku1 = Sudoku(values1)
print('Values to solve ',sudoku1)
sudoku1.solve()
print('Solved table ', sudoku1)

sudoku2 = Sudoku(values2)
print('Values to solve ',sudoku2)
sudoku2.solve()
print('Solved table ', sudoku2)
