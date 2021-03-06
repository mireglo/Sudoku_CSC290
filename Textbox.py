import pygame
import GameScreen


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

    def set_active(self):
        self._active = True

    def set_inactive(self):
        self._active = False

    def handle_event(self, event):
        # Handles mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check that the Textbox can be edited
            if self._editable:
                self._colour = (0, 10, 100)
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

    def is_editable(self):
        return self._editable

    def handle_int_event(self, event):
        # Handles mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Check that the Textbox can be edited
            if self._editable:
                # Check where the user clicked
                if self._input_box.collidepoint(event.pos):
                    if(0 <= (event.pos[0]-40)//40 <= 8 and 0 <=
                            (event.pos[1]-40)//40 <= 8):
                        GameScreen.set_current_tile = [(event.pos[0]-40)//40,
                                                (event.pos[1]-40)//40]
                    # Toggle the active variable
                    self._active = True
                else:
                    self._active = False
            else:
                self._active = False
        # Handles keyboard events
        if event.type == pygame.KEYDOWN and self._editable and self._active:
            # Make changes to the text
            if event.key == pygame.K_BACKSPACE:
                self._text = self._text[:-1]
            else:
                if len(self._text) >= 0 \
                        and (event.unicode in
                             ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
                    self._text = event.unicode
