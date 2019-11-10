import os
import GridDraw
from Textbox import*
from Sudoku import*


class SDKuPGApplication:
    """ The SDKuPG game application

    === Private Attributes ===
    _grid:
        The game of Sudoku
    _rect:
        The rectangle the screen is made from
    _screen:
        The game screen
    """
    def __init__(self, width, height):
        """ Initializes the game application
        """
        self._rect = pygame.Rect(0, 0, width, height)
        self._grid = Sudoku()
        pygame.init()
        pygame.display.set_caption("SDKuPG")
        self._screen = pygame.display.set_mode(self._rect.size)

        padding = 20

        self._text_grid = [[None for _ in range(9)] for _ in range(9)]
        # Create a Textbox for each cell of the grid
        for row in range(9):
            for col in range(9):
                self._text_grid[row][col] = \
                    Textbox((width - 2 * padding) * col/9 + padding,
                            (height - 2 * padding) * row/9 + padding,
                            (width - 2 * padding) * 1/9,
                            (height - 2 * padding) * 1/9)

        # Reads the grid model and displays each cell on the screen
        for row in range(9):
            for col in range(9):
                # 0 is seen as an empty space, and the clues
                if self._grid.get_cell(row, col) != 0:
                    self._text_grid[row][col].set_text(self._grid.get_cell(row,
                                                                           col))
                    self._text_grid[row][col].set_editable(False)

    def _update_screen(self):
        """ Restarts the grid to the initial grid
        """
        for row in range(9):
            for col in range(9):
                if self._grid.get_cell(row, col) != 0:
                    self._text_grid[row][col].set_text(self._grid.get_cell(row,
                                                                           col))
                else:
                    self._text_grid[row][col].set_text("")

    @staticmethod
    def _draw_background(screen):
        """ Draws the background as white
        """
        screen.fill((255, 255, 255))

    @staticmethod
    def _draw_game():
        """ Draws the sudoku game using GridDraw functions
        """
        GridDraw.draw_box()
        GridDraw.draw_grid()

    def launch(self):
        """ Launches the game application
        """
        clock = pygame.time.Clock()

        running = True

        while running:

            # --- events ---

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_r:
                        self._grid.restart()
                        self._update_screen()
                    # if event.key == pygame.K_u:
                    #     self._grid.undo_fill()
                    #     self._update_screen()

                for row in range(9):
                    for col in range(9):
                        self._text_grid[row][col].handle_int_event(event)
                        change = self._text_grid[row][col].get_text()
                        if change == "":
                            change = 0
                        self._grid.fill(int(change), row, col)

            # --- draws ---

            self._draw_background(self._screen)
            self._draw_game()
            for sublist in self._text_grid:
                for textbox in sublist:
                    textbox.draw(self._screen)
            pygame.display.update()

            # --- FPS ---

            clock.tick(50)  # 25 Frames Per Seconds

        pygame.quit()
        os._exit(0)


# To check the class works as intended.
if __name__ == "__main__":
    SDKuPGApplication(500, 500).launch()