import pygame


class MainMenu:
    """ The MainMenu class represents the main menu screen for this game.

    === Private Attributes ===
    _screen:
        Where the visuals are displayed
    _current_screen:
        Holds the current screen state the game is on
    _blue2:
        Colours used for draw_ufo
    _silver2:
        Colours used for draw_ufo
    _silver3:
        Colours used for draw_ufo
    """

    def __init__(self, screen) -> None:
        """
        Initialize an empty main menu screen.
        """
        self._screen = screen
        self._current_screen = "Menu"
        self._blue2 = (137, 236, 255)
        self._silver2 = (171, 170, 169)
        self._silver3 = (210, 210, 210)
        return

    def draw_ufo(self) -> None:
        """
        Draw the ufo on the screen which is used as a cursor for the main menu.
        """
        x, y = pygame.mouse.get_pos()
        pygame.draw.ellipse(self._screen, self._silver3,
                            [-28 + x, -13 + y, 55, 25],
                            0)
        pygame.draw.ellipse(self._screen, self._blue2,
                            [-18 + x, -16 + y, 35, 18], 0)
        pygame.draw.ellipse(self._screen, self._silver2, [-20 + x, 0 + y, 3, 5],
                            0)
        pygame.draw.ellipse(self._screen, self._silver2, [-8 + x, 4 + y, 3, 5],
                            0)
        pygame.draw.ellipse(self._screen, self._silver2, [4 + x, 4 + y, 3, 5],
                            0)
        pygame.draw.ellipse(self._screen, self._silver2, [16 + x, 0 + y, 3, 5],
                            0)

    def add_buttons(self) -> None:
        """
        Add play and quit buttons to the main menu screen.
        """
        # Add background colour
        self._screen.fill((255, 235, 186))
        # Add Play button
        pygame.draw.circle(self._screen, (0, 255, 0), (365, 250), 70, 5)
        title_font = pygame.font.SysFont('Comic Sans MS', 60)
        text_surface = title_font.render('Play', True, (0, 255, 0))
        self._screen.blit(text_surface, (325, 230))
        # Add quit button
        pygame.draw.circle(self._screen, (255, 0, 0), (135, 250), 70, 5)
        title_font = pygame.font.SysFont('Comic Sans MS', 60)
        text_surface = title_font.render('Quit', True, (255, 0, 0))
        self._screen.blit(text_surface, (91, 230))
        # Update screen
        pygame.display.update()

    def design_menu_title(self) -> None:
        """
        Add menu title to main menu screen.
        """
        # Add game title
        title_font = pygame.font.SysFont('Comic Sans MS', 125)
        text_surface = title_font.render('SDKuPG', True, (0, 155, 255))
        self._screen.blit(text_surface, (75, 50))

    def add_action_listeners(self) -> None:
        """
        Keeps track of the mouses position in order to update whether user
        wishes to quit game or play game. Sets self.current_screen state.
        """
        x, y = pygame.mouse.get_pos()
        if (310 < x < 420) and (200 < y < 300):
            self._current_screen = "Game"
        if (90 < x < 180) and (200 < y < 300):
            self._current_screen = "None"

    def get_current_screen(self) -> str:
        """
        Getter method for self.current_screen. Returns which screen game is on.
        """
        return self._current_screen

    def set_current_screen(self, s: str) -> None:
        """
        Setter method for self.current_screen. Sets self.current_screen to
        the state this game is on.
        """
        self._current_screen = s

    def launch_menu(self) -> None:
        """
        Launches all the menu components to set up menu when called.
        """
        self.add_buttons()
        self.design_menu_title()
        self.draw_ufo()
        self.add_action_listeners()
