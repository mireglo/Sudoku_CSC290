from GameScreen import*
import GridDraw
import sys


class SDKuPGApplication:
    """ The SDKuPG game application

    === Private Attributes ===
    _rect:
        The rectangle the screen is made from
    _screen:
        Where the visuals are displayed
    _game_screen:
        A GameScreen that draws the game
    """
    def __init__(self, width, height):
        """ Initializes the game application
        """
        pygame.init()
        pygame.display.set_caption("SDKuPG")
        self._rect = pygame.Rect(0, 0, width, height)
        self._screen = pygame.display.set_mode(self._rect.size)
        self._game_screen = GameScreen(self._screen)

    @staticmethod
    def _draw_background(screen):
        """ Draws the background as white
        """
        screen.fill((255, 255, 255))

    @staticmethod
    def _draw_game(self):
        """ Draws the sudoku game using GridDraw functions
        """
        self._game_screen.draw_grid(self._screen)
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
                self._game_screen.handle_game(event)

            # --- draws ---

            self._draw_background(self._screen)
            self._draw_game(self)
            pygame.display.update()

            # --- FPS ---

            clock.tick(50)

        pygame.quit()
        sys.exit(0)


# To check the class works as intended.
if __name__ == "__main__":
    SDKuPGApplication(500, 500).launch()
