import pygame
import os

# Width of the application window
screen_width = 500
# Height of the application window
screen_height = 500
# Padding space between window edges and puzzle
padding = 20

# Color tuples
white_color = (255, 255, 255)
black_color = (0, 0, 0)

screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill(white_color)

def draw_box():
    '''
    This function is used to draw the outer box of the sudoku puzzle
    '''
    pygame.draw.line(screen, black_color, (padding, padding),                            (padding, screen_height-padding), 2)
    pygame.draw.line(screen, black_color, (padding, padding),                            (screen_width-padding, padding),  2)
    pygame.draw.line(screen, black_color, (screen_width-padding, screen_height-padding), (padding, screen_height-padding), 2)
    pygame.draw.line(screen, black_color, (screen_width-padding, screen_height-padding), (screen_width-padding, padding),  2)
    
def draw_grid():
    '''
    This function is used to draw the inner grid as well as all the cells of the sudoku puzzle.
    
    The main 9 boxes of the grid are drawn with a thicker line so as to make it easier to differentiate them from one another
    '''
    for i in range(1, 9):
        
        if i % 3 == 0:
            thick = 2
            
        else:
            thick = 1
        
        # Drawing Vertical Lines
        line_x = ((screen_width-(2*padding))*i/9) + padding
    
        pygame.draw.line(screen, 
                         black_color, 
                         (line_x, padding),
                         (line_x, screen_height-padding),
                         thick)
        
        #Drawing Horizontal lines
        line_y = ((screen_height-(2*padding))*i/9) + padding
        
        pygame.draw.line(screen,
                         black_color,
                         (padding, line_y),
                         (screen_width-padding, line_y),
                         thick)

# To Test whether the code is working uncomment and run the below lines. You should get an empty puzzle drawn.

# if __name__ == '__main__':
    
    # draw_box()
    # draw_grid()

    # while True:
    
        # pygame.display.update()
        
        # for event in pygame.event.get():
            # if event.type == pygame.QUIT:
                # pygame.quit()
                # os._exit(0)
        