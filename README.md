# SDKuPG (Sudoku Puzzle Game)

## Installation

Install ``Python 3.0`` or greater. From there, run the command ``pip install pygame`` in the shell. Finally, git clone or download the repository and run ``SDKuPGApplication.py`` through an IDE or CLI of choice to run the game.

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

## License

MIT License (MIT)

Copyright © 2019 Steve Group

You can find a copy of the licence at https://mit-license.org/
