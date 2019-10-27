"""
The purpose of this class is to handle parsing input from the board or any
screen that requires it
"""
from GridAccess import*

class InputHandler:

    def __init__(self):
        return

    def change_board(self, row, col, change, grid):
        if self.is_valid_change(change):
            grid.change_display_gird(row, col, change)
        return

    def is_valid_change(self, intake):
        if len(intake) > 1:
            return False
        if not isinstance(intake, int):
            return False
        if isinstance(intake, int) and int(intake) == 0:
            return False
        return True
