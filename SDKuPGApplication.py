from GameScreen import*
from MainMenu import*
import sys


class SDKuPGApplication:
    """ The SDKuPG game application

    === Private Attributes ===
    _rect:
        The rectangle the screen is made from
    _screen:
        Where the visuals are displayed
    _game_screen:
        A GameScreen that can draw and handle events for the game
    _main_menu:
        A MainMenu that can draw and handle events for the main menu
    """
    def __init__(self, width, height):
        """ Initializes the game application
        """
        pygame.init()
        pygame.display.set_caption("SDKuPG")
        self._rect = pygame.Rect(0, 0, width, height)
        self._screen = pygame.display.set_mode(self._rect.size)
        self._game_screen = GameScreen(self._screen)
        self._main_menu = MainMenu(self._screen)
        self._menus = {}
        lst = ["on_game_screen", "on_game_screen"]
        for menu in lst:
            self._menus[menu] = False
        self._menus["on_main_menu"] = True

    @staticmethod
    def _draw_background(screen):
        """ Draws the background as white
        """
        screen.fill((255, 255, 255))

    def _change_menu(self, menu):
        """ Sets all other menus to false, sets given menu to True
        """
        if menu in self._menus:
            for key in self._menus.keys():
                if key != menu:
                    self._menus[key] = False
                else:
                    self._menus[key] = True

    def launch(self):
        """ Launches the game application
        """
        clock = pygame.time.Clock()

        running = True

        while running:

            # --- mouse events ---
            if self._main_menu.get_current_screen() == "None":
                running = False
            if self._main_menu.get_current_screen() == "Game":
                self._change_menu("on_game_screen")

            # --- events ---

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_n:
                        self._change_menu("on_game_screen")
                    if event.key == pygame.K_m:
                        self._change_menu("on_main_menu")
                        self._main_menu.set_current_screen("Menu")
                if self._menus["on_game_screen"]:
                    self._game_screen.handle_game(event)

            # --- draws ---

            self._draw_background(self._screen)
            if self._menus["on_game_screen"]:
                self._game_screen.draw_game(self._screen)
            if self._menus["on_main_menu"]:
                pygame.mouse.set_visible(0)
                self._main_menu.launch_menu()
            else:
                pygame.mouse.set_visible(1)
            pygame.display.update()

            # --- FPS ---

            clock.tick(25)

        pygame.quit()
        sys.exit(0)


# To check the class works as intended.
if __name__ == "__main__":
    SDKuPGApplication(500, 500).launch()
