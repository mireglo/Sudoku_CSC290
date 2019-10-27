"""
The purpose of this class is to extract a grid from SudokuGrid and use it as
the and to hold the playergrid
"""
from SudokuGrid import*


class GridAccess:
    def __init__(self):
        self._sol = []
        self._disp = []

    def new_grid(self):
        freshgrid = SudokuGrid()
        for _ in range(9):
            self._sol.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
            self._disp.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        freshgrid.create_solution()
        for row in range(9):
            for col in range(9):
                self._sol[row][col] = (int(freshgrid.get_cell(row, col)))

        freshgrid.hide_numbers()
        for row in range(9):
            for col in range(9):
                self._disp[row][col] = int(freshgrid.get_cell(row, col))

    def get_display_grid(self):
        return self._disp

    def change_display_grid(self, row, col, change):
        self._disp[row][col] = change
        if self.game_over():
            print("winner")
            #will implement game stop and flash win screen
        return

    def game_over(self):
        win = True
        for row in range(9):
            for col in range(9):
                if self._disp[row][col] is not self._sol[row][col]:
                    win = False
        return win
