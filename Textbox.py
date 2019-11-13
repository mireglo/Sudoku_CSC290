import pygame


class Textbox:
    """ A textbox to allow user input

    === Private Attributes ===
    _colour:
        The RGB colour value of the text and input_box
    _font:
        The font of the text
    _input_box:
        The rectangle the Textbox is represented as
    _active:
        Whether the user selected this Textbox
    _editable:
        Whether the text can be changed
    _text:
        The text that is displayed
    """
    current_tile = [0, 0]

    def __init__(self, x_pos, y_pos, width, height):
        self._colour = (0, 0, 0)
        self._font = pygame.font.SysFont("Calibri", 50, True, False)
        self._input_box = pygame.Rect(x_pos, y_pos, width, height)
        self._active = False
        self._editable = True
        self._text = ''

    def set_text(self, change):
        self._text = str(change)

    def get_text(self):
        return self._text

    def set_editable(self, editable):
        if isinstance(editable, bool):
            self._editable = editable

    def draw(self, screen):
        # Render the current text
        txt_surface = self._font.render(self._text, True, self._colour)

        # Blit / add the text to screen
        if self._active:
            pygame.draw.rect(screen, (194, 245, 255), self._input_box)
        screen.blit(txt_surface, (self._input_box.x+13, self._input_box.y+2))

    def handle_event(self, event):
        # Handles mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check that the Textbox can be edited
            if self._editable:
                self._colour = (0,10,100)
                # Check where the user clicked
                if self._input_box.collidepoint(event.pos):
                    # Toggle the active variable
                    self._active = True
                else:
                    self._active = False
        # Handles keyboard events
        if event.type == pygame.KEYDOWN:
            if self._active:
                # Make changes to the text
                if event.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                else:
                    self._text += event.unicode

       # def handle_nav_event(self, event):
    #     # Handles navigation with WASD keys
    #     if event.type == pygame.KEYUP:
    #         #down arrow
    #         if event.key == pygame.K_s and Textbox.current_tile[0] != 8:
    #             Textbox.current_tile[0] = Textbox.current_tile[0] + 1
    #         #up arrow
    #         elif event.key == pygame.K_w and Textbox.current_tile[0] != 0:
    #             Textbox.current_tile[0] = Textbox.current_tile[0] - 1
    #         #right arrow
    #         elif event.key == pygame.K_d and Textbox.current_tile[1] != 8:
    #             Textbox.current_tile[1] = Textbox.current_tile[1] + 1
    #         #left arrow
    #         elif event.key == pygame.K_a and Textbox.current_tile[1] != 0:
    #             Textbox.current_tile[1] = Textbox.current_tile[1] - 1
    #         print(Textbox.current_tile)

    def handle_int_event(self, event):
        # Handles mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Check that the Textbox can be edited
            if self._editable:
                # Check where the user clicked
                if self._input_box.collidepoint(event.pos):
                    if(0 <= (event.pos[0]-40)//40 <= 8 and 0 <=
                            (event.pos[1]-40)//40 <= 8):
                        Textbox.current_tile = [(event.pos[0]-40)//40,
                                                (event.pos[1]-40)//40]
                    # Toggle the active variable
                    print(Textbox.current_tile)
                    self._active = True
                else:
                    self._active = False
        # Handles keyboard events
        if event.type == pygame.KEYDOWN:
            if self._active:
                # Make changes to the text
                if event.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                elif event.key == pygame.K_s and Textbox.current_tile[0] != 8:
                    Textbox.current_tile[0] = Textbox.current_tile[0] + 1
                # up arrow
                elif event.key == pygame.K_w and Textbox.current_tile[0] != 0:
                    Textbox.current_tile[0] = Textbox.current_tile[0] - 1
                # right arrow
                elif event.key == pygame.K_d and Textbox.current_tile[1] != 8:
                    Textbox.current_tile[1] = Textbox.current_tile[1] + 1
                # left arrow
                elif event.key == pygame.K_a and Textbox.current_tile[1] != 0:
                    Textbox.current_tile[1] = Textbox.current_tile[1] - 1
                else:
                    if len(self._text) >= 0 \
                            and (event.unicode in
                                 ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
                        self._text = event.unicode
                print(Textbox.current_tile)
