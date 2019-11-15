import pygame


class MainMenu:

    def __init__(self):
        self._blue2 = (194, 245, 255)
        self._silver2 = (171, 170, 169)
        self._silver3 = (210, 210, 210)
        return

    def draw_ufo(self, screen):
        x, y = pygame.mouse.get_pos()
        pygame.draw.ellipse(screen, self._silver3, [-28 + x, -13 + y, 55, 25], 0)
        pygame.draw.ellipse(screen, self._blue2, [-18 + x, -16 + y, 35, 18], 0)
        pygame.draw.ellipse(screen, self._silver2, [-20 + x, 0 + y, 3, 5], 0)
        pygame.draw.ellipse(screen, self._silver2, [-8 + x, 4 + y, 3, 5], 0)
        pygame.draw.ellipse(screen, self._silver2, [4 + x, 4 + y, 3, 5], 0)
        pygame.draw.ellipse(screen, self._silver2, [16 + x, 0 + y, 3, 5], 0)
