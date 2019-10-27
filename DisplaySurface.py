import pygame, os
import GridDraw

# DisplaySurface class
class DisplaySurface():

    def __init__(self, width, height):
        ''' Initializes the display surface
        '''
        self.rect = pygame.Rect(0, 0, width, height)
        pygame.init()
        pygame.display.set_caption("SDKuPG")
        self.screen = pygame.display.set_mode(self.rect.size)
        

    def draw_background(self, screen):
        ''' Draws the background as white
        '''
        screen.fill((255,255,255))


    def draw_game(self):
        ''' Draws the sudoku game using GridDraw functions
        '''
        GridDraw.draw_box()
        GridDraw.draw_grid()


    def run(self):
        ''' Logic for changing screens
        '''
        clock = pygame.time.Clock()

        RUNNING = True

        while RUNNING:

            #--- events ---

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    RUNNING = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        RUNNING = False

            #--- draws ---

            self.draw_background(self.screen)
            self.draw_game()
            pygame.display.update()

            #--- FPS ---

            clock.tick(25) # 25 Frames Per Seconds

        pygame.quit()
        os._exit(0)

# To check the class works as intended.

if __name__ == "__main__":
    DisplaySurface(500,500).run()
