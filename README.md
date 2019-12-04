# SDKuPG (Sudoku Puzzle Game)

## Installation

Install Python 3.0 or greater. From there, run pip install pygame in the shell. Finally, git clone or download the repository and run the game through an IDE or CLI of choice.  

## Rules of Sudoku

When you start the game, you get a board which has a 9x9 grid of cells. This grid is partially filled with numbers from 1-9. The goal of the game is to fill the grid completely while following the following rules:

* A row can only have one instance of a number from 1 to 9

For Example:

![RowExample](https://user-images.githubusercontent.com/29599132/70167835-90976300-1695-11ea-9101-972a24cc70dd.png)

Here this row has every number between 1 and 9 except 3. So the only possible way to fill this cell is by entering 3.

* A column can only have one instance of a number from 1 to 9

![ColumnExample](https://user-images.githubusercontent.com/29599132/70168187-5e3a3580-1696-11ea-9a30-c05c22d99834.png)

Here this column has every number between 1 and 9 except 1. So the only possible way to fill this cell is by entering 1.

* A 3x3 sub grid (also known as a block) can only have one instance of a number from 1 to 9

![BlockExample](https://user-images.githubusercontent.com/29599132/70168261-81fd7b80-1696-11ea-89ba-8c016d133787.png)

Here this block has every number between 1 and 9 except 2. So the only possible way to fill this cell is by entering 2.

## How to Play

The game screen display a 9x9 Sudoku board which will have some cells automatically filled with a number. You have to fill in the rest of the cells while following the rules. To do so use the following controls:

* Click on a 1x1 cell or move to it using the WASD to select it.
  * W moves one cell up
  * S moves one cell down
  * A moves one cell left
  * D moves one cell right

* The current cell is highlighted by a light blue tint. An example is shown below:

  * Before selecting the cell
  
  ![Pre-Highlight](https://user-images.githubusercontent.com/29599132/70168672-4e6f2100-1697-11ea-864c-0bb40d00b13f.png)
  
  * After selecting the cell
  
  ![Post-Highlight](https://user-images.githubusercontent.com/29599132/70168678-516a1180-1697-11ea-9b8c-4c34dd4cc296.png)
  
* Press a 1-9 numeric key to make an entry into the board or press Backspace to remove the number from the cell.

* Click the Main Menu button to return to the main menu. This will not reset the game as the board will stay unchanged.

The game will end once the board is completely filled according to the rules, after which it will proceed to the "game won" screen".

## Contributors

## License

MIT License (MIT)

Copyright © 2019 Steve Group

You can find a copy of the licence at https://mit-license.org/
