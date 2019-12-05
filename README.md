# SDKuPG (Sudoku Puzzle Game)

## Installation

If you don't already have ```Python 3.0``` or greater installed, head on over [here](https://www.python.org/downloads/) to install ```Python 3.0``` or greater. From there, run the command ``pip install pygame`` in the shell to install the ``Pygame`` module. Finally, [git clone](https://github.com/mireglo/Sudoku_CSC290) or [download](https://github.com/mireglo/Sudoku_CSC290) the repository and run the file ``SDKuPGApplication.py`` through an IDE or CLI of choice to play the game.

##### To clone, paste this into your shell: ``git clone https://github.com/mireglo/Sudoku_CSC290.git``

## Rules of Sudoku

When you start the application, a window will open up displaying a board with a 9x9 grid of cells. The 9x9 grid is further divided into a 3x3 grids indicated by the thicker borders. The grid is partially filled with numbers from 1-9. The goal of the game is to fill the grid completely while maintaining the following rules:

* **A row can only have one instance of a number from 1 to 9**

Here the row with the highlighted cell has every number between 1 and 9 except 3. So the only possible way to fill this cell is by entering a 3.

![RowExample](https://user-images.githubusercontent.com/29599132/70167835-90976300-1695-11ea-9101-972a24cc70dd.png)

* **A column can only have one instance of a number from 1 to 9**

Here the column with the highlighted cell has every number between 1 and 9 except 1. So the only possible way to fill this cell is by entering a 1.

![ColumnExample](https://user-images.githubusercontent.com/29599132/70168187-5e3a3580-1696-11ea-9a30-c05c22d99834.png)

* **A 3x3 subdivision (also known as a block) can only have one instance of a number from 1 to 9**

Here the block with the highlighted cell has every number between 1 and 9 except 2. So the only possible way to fill this cell is by entering 2.

![BlockExample](https://user-images.githubusercontent.com/29599132/70168261-81fd7b80-1696-11ea-89ba-8c016d133787.png)

## How to Play

The game screen display a 9x9 Sudoku board which will have some cells automatically filled with a number.
You have to fill in the rest of the cells while following the rules. To do so use the following controls:

* The current selected cell is highlighted with light blue tint. An example is shown below:

  * Before selecting the cell

  ![Pre-Highlight](https://user-images.githubusercontent.com/29599132/70168672-4e6f2100-1697-11ea-864c-0bb40d00b13f.png)

  * After selecting the cell

  ![Post-Highlight](https://user-images.githubusercontent.com/29599132/70168678-516a1180-1697-11ea-9b8c-4c34dd4cc296.png)

* To select a cell, click on the cell or move to the cell from the current selection using the WASD
  * W moves one cell up
  * S moves one cell down
  * A moves one cell left
  * D moves one cell right

* Press a numeric key (1-9) to make an entry into the board or press BACKSPACE to remove the number from the cell

* Click the ``Main Menu`` button to return to the main menu. This will not reset the game as the board will stay unchanged

The game will end once the board is completely filled according to the rules, after which it will proceed to the "game won screen".

## Contributors

- **Hamzah Shahid**
    - I created the MainMenu class for our game which allows users to smoothly transition from and to the game screen. I fixed bugs that existed in the SDKuPGApplication.py class too. In addition to this, I am responsible for testing the code to ensure that everything works the way that it should. Furthermore, I created the GameButton.py class which is currently unused. This class will be used for further implementations where someone may wish to add extra functionalities to the sudoku board such as changing the colours of pieces. Within this README file, I was responsible for relaying to potential users how to install our game. Additionally, I explained a portion of our gameplay and added the MIT license.
    
- **Arsh Khan**
   - I created the GridDraw module which allows you to draw the grid for the puzzle. I also added the ability to use the arrow keys as a control scheme. Finally I fixed a bug with the game not highlighting the first selected cell. For the README, I added the 'Rules of Sudoku' section. I also fleshed out the 'How to Play' section.

- **Anthony Lee**
   - I created SudokuApplication and Textbox. The application launches the game and acts as the view. Creating the application involved hooking up the game to the GUI. Additionally, I made the UFO cursor in the menu screen. The textboxes represent an individual cell and can get input. Fixed a bug where using the arrow keys did not highlight a clue cell.


## License

MIT License (MIT)

Copyright © 2019 Steve Group

You can find a copy of the licence at https://mit-license.org/
