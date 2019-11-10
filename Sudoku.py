"""
The purpose of this class is to extract a grid from SudokuGrid and use it as
the and to hold the playergrid
"""
from SudokuGrid import*


class Sudoku:
    def __init__(self):
        self._grid = SudokuGrid()
        self._grid.start_game(5)

    # def get_display_grid(self):
    #     return self._grid._grid_display dont do this

    def change_display_grid(self, n, row, col):
        self._grid.change_board(n, row, col)
            #will implement game stop and flash win screen
        return

    def restart(self):
        return self._grid.reset()

    def get_cell(self, row, col):
        return self._grid.get_cell(row, col)

    def game_over(self):
        return self._grid.game_over()
