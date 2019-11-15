import pygame
import GridDraw
from Textbox import*
from Sudoku import*


class GameScreen:
    """ Controls the game

    === Private Attributes ===
    _grid:
        The game of Sudoku
    _text_grid:
        A grid that keeps track of each textbox
    """
    current_tile = [0, 0]

    def __init__(self, screen):
        """ Initializes the game application
        """
        self._grid = Sudoku()
        # self._screen = screen
        padding = 20
        width, height = screen.get_size()

        self._text_grid = [[None for _ in range(9)] for _ in range(9)]
        # Create a Textbox for each cell of the grid
        for row in range(9):
            for col in range(9):
                self._text_grid[row][col] = \
                    Textbox((width - 2 * padding) * col / 9 + padding,
                            (height - 2 * padding) * row / 9 + padding,
                            (width - 2 * padding) * 1 / 9,
                            (height - 2 * padding) * 1 / 9)

        # Reads the grid model and displays each cell on the screen
        for row in range(9):
            for col in range(9):
                # 0 is seen as an empty space, and the clues
                if self._grid.get_cell(row, col) != 0:
                    self._text_grid[row][col].set_text(self._grid.get_cell(row,
                                                                           col))
                    self._text_grid[row][col].set_editable(False)

    def _update_screen(self):
        """ Updates the view to represent the current state of the board
        """
        for row in range(9):
            for col in range(9):
                if self._grid.get_cell(row, col) != 0:
                    self._text_grid[row][col].set_text(self._grid.get_cell(row,
                                                                           col))
                else:
                    self._text_grid[row][col].set_text("")

    def deactivate_all(self):
        for row in range(9):
            for col in range(9):
                self._text_grid[row][col].set_deactive()

    def _update_tile(self):
        self.deactivate_all()
        if self._text_grid[GameScreen.current_tile[0]][GameScreen.current_tile[1]].is_editable():
            self._text_grid[GameScreen.current_tile[0]][GameScreen.current_tile[1]].set_active()

    def handle_game(self, event):
        """ Handles user inputs
        """
        # Handles keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self._grid.restart()
                self._update_screen()
            if event.key == pygame.K_u:
                self._grid.undo_fill()
                self._update_screen()
            if event.key == pygame.K_s and GameScreen.current_tile[0] != 8:
                GameScreen.current_tile[0] = GameScreen.current_tile[0] + 1
                self._update_tile()
                # up arrow
            if event.key == pygame.K_w and GameScreen.current_tile[0] != 0:
                GameScreen.current_tile[0] = GameScreen.current_tile[0] - 1
                self._update_tile()

            # right arrow
            if event.key == pygame.K_d and GameScreen.current_tile[1] != 8:
                GameScreen.current_tile[1] = GameScreen.current_tile[1] + 1
                self._update_tile()

            # left arrow
            if event.key == pygame.K_a and GameScreen.current_tile[1] != 0:
                GameScreen.current_tile[1] = GameScreen.current_tile[1] - 1
                self._update_tile()

        for row in range(9):
            for col in range(9):
                self._text_grid[row][col].handle_int_event(event)
                change = self._text_grid[row][col].get_text()
                if change == "":
                    change = 0
                self._grid.fill(int(change), row, col)

    def draw_game(self, screen):
        """ Draws the sudoku game using GridDraw functions
        """
        for sublist in self._text_grid:
            for textbox in sublist:
                textbox.draw(screen)
        GridDraw.draw_box()
        GridDraw.draw_grid()
