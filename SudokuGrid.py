from random import randint, shuffle
from typing import List, Optional


NUMLIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0


class SudokuGrid:

    def __init__(self) -> None:
        '''Initializing a SudokuGrid with an empty grid
        '''
        self._grid = []
        for _ in range(9):
            self._grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

    @staticmethod
    def check_valid_placement(n: int, row: int, col: int, grid: List) -> bool:
        '''Returns if n is already in row, col or in the square containing
        (row,col).
        '''
        if SudokuGrid.in_square(n, row, col, grid) or \
                SudokuGrid.in_row(n, row, col, grid) or \
                SudokuGrid.in_col(n, row, col, grid):
            return True
        return False

    @staticmethod
    def in_square(n: int, row: int, col: int, grid: List) -> bool:
        '''Return if n is in the square containing (row, col)
        '''
        for sub_row in range((row//3)*3, (row//3 + 1)*3):
            for sub_col in range((col//3)*3, (col//3 + 1)*3):
                if sub_row != row and sub_col != col and \
                        grid[sub_row][sub_col] == n:
                    return True
        return False

    @staticmethod
    def in_row(n: int, row: int, col: int, grid: List) -> bool:
        '''Return if n is in row of the grid
        '''
        for x in range(9):
            if x != col and n == grid[row][x]:
                return True
        return False

    @staticmethod
    def in_col(n: int, row: int, col: int, grid: List) -> bool:
        '''Return if n is in col of the grid
        '''
        for x in range(9):
            if x!= row and n == grid[x][col]:
                return True
        return False

    @staticmethod
    def check_grid(grid: List):
        '''Return if grid is filled
        '''
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    return False
        return True

    def create_solution(self) -> bool:
        '''Recursively constructs a puzzle solution
        '''
        row = 0
        col = 0
        for i in range(81):
            # current cell
            row = i // 9
            col = i % 9

            # if cell is empty we try placing number in it
            if self._grid[row][col] == 0:
                shuffle(NUMLIST)
                for n in NUMLIST:

                    # if n is viable for placement for cell then place it
                    if not SudokuGrid.check_valid_placement(n, row, col,
                                                            self._grid):
                        self._grid[row][col] = n

                        # check if grid is full and return true
                        if SudokuGrid.check_grid(self._grid):
                            return True

                        # otherwise recurse to place next cell
                        elif self.create_solution():
                            return True

                # break loop if no valid placement in cell
                break

        # will set current cell to 0 and go back to previous recursion
        # to find another valid cell placement combination
        self._grid[row][col] = 0
        return False

    def hide_numbers(self):
        '''Removes cells while maintaining a unique solution
        '''
        global counter

        # num of attempts allow for more blocks to be removed
        attempts = 2

        while attempts > 0:
            # selecting random cell and rotational counterpart
            row = randint(0, 8)
            col = randint(0, 8)
            while self._grid[row][col] == 0:
                row = randint(0, 8)
                col = randint(0, 8)

            # backing up in case removal is gives multiple solutions
            backupone = self._grid[row][col]
            backuptwo = self._grid[8 - row][8 - col]
            self._grid[row][col] = 0
            self._grid[8 - row][8 - col] = 0

            # cloning grid to test number of solutions
            test_puzzle = []
            for r in range(0, 9):
                test_puzzle.append(self._grid[r][:])

            # counter for num solutions is set to 0
            counter = 0

            # check num of solutions
            self.solve_puzzle(test_puzzle)

            print(counter)
            # if num of solutions is not one, replace the two blocks
            if counter != 1:
                self._grid[row][col] = backupone
                self._grid[8 - row][8 - col] = backuptwo
                attempts -= 1

    def solve_puzzle(self, test_puzzle) -> bool:
        '''Attempts to solve puzzle using all possible solution combinations
        '''
        global counter
        row = 0
        col = 0
        for i in range(81):
            # current cell
            row = i // 9
            col = i % 9

            # if cell is empty we check to see possible placements
            if test_puzzle[row][col] == 0:
                # trying to place number in current cell
                for n in range(1, 10):

                    # checking if we can place n in current cell
                    if not SudokuGrid.check_valid_placement(n, row, col,
                                                            test_puzzle):
                        # placing n in cell
                        test_puzzle[row][col] = n

                        # check if grid is full increment number of solutions
                        # and break loop to go to previous recursions to try
                        # other combinations
                        if SudokuGrid.check_grid(test_puzzle):
                            counter += 1
                            break

                        # otherwise recurse to place next cell
                        elif self.solve_puzzle(test_puzzle):
                            return True

                # break loop if no valid placement in cell
                break

        # will set current square to 0 and go back to previous recursion
        # to find another valid placement
        test_puzzle[row][col] = 0
        return False

    def change_board(self, n: int, row: int, col: int) -> bool:
        '''Return if move was made successfully
        '''
        if self._grid[row][col] == 0:
            self._grid[row][col] = n
            return True
        return False

    def game_over(self) -> bool:
        '''Return if board state is a valid solution

        PRECONDITION: this is ran if SudokuGrid.check_grid(grid) == True
        '''
        for row in range(9):
            for col in range(9):
                n = self._grid[row][col]
                if not SudokuGrid.check_valid_placement(n, row, col,
                                                        self._grid):
                    return False
        return True

    def __str__(self) -> str:
        '''Producing string of matrix for visualization
        '''
        string = ''
        for row in self._grid:
            string += row.__str__() + '\n'
        return string


if __name__ == "__main__":
    # initializing empty grid
    sudokugrid = SudokuGrid()
    print(sudokugrid)

    # creating puzzle solution
    sudokugrid.create_solution()
    print(sudokugrid)

    # hiding numbers to make solvable puzzle
    sudokugrid.hide_numbers()
    print(sudokugrid)
