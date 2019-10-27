from typing import Tuple


class GameButton:

    def __init__(self, row: int, col: int, state: int, change: bool) -> None:
        '''Initializing a GameButton used to represent game pieces
        '''
        self._row = row
        self._col = col
        self._state = state
        self._is_changeable = change

    def get_state(self) -> int:
        '''Return the value stored in this button
        '''
        return self._state

    def get_changeable(self) -> bool:
        '''Return whether this buttons state can be changed
        '''
        return self._is_changeable

    def get_position(self) -> Tuple[int, int]:
        '''Return the (row, col) of this button
        '''
        return self._row, self._col

    def update_button(self, value: int) -> None:
        '''Update the state of this button according to input
        '''
        if self.valid_update(value):
            self._state = value

    def valid_update(self, value: int) -> bool:
        '''Return whether this update can be made
        '''
        return 0 <= value <= 9 and \
               value != self.get_state() and \
               self.get_changeable()


if __name__ == "__main__":
    # create a GameButton instance that can change state
    a = GameButton(0, 0, 4, True)
    # update to value
    old = a.get_state()
    a.update_button(2)
    # show new value
    print(f"New Value: {a.get_state()}, Old Value: {old}")

    # create a GameButton instance that can change state
    a = GameButton(0, 0, 4, False)
    # attempt to update value
    old = a.get_state()
    a.update_button(2)
    # show value
    print(f"New Value: {a.get_state()}, Old Value: {old}")
