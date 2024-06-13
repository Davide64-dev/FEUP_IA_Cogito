# Artificial Intelligence

The development of this program is part of the curriculum for the [Artificial Intelligence](https://sigarra.up.pt/feup/en/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=520334) course.

## Running:
Start the game by:

```sh
pip install -r requirements.txt
```

```sh
cd src
```

```sh
python3 main.py
```

### Optional - create a virtual environment (installs packages only locally in the project)

```sh
python -m venv venv
```
```sh
source venv/bin/activate
```

to exit: 

```sh
deactivate
```

You are then presented with a menu that will allow to choose between the regular gameplay mode, or between a selection of implemented algorithms that will try to solve the levels by themselves.

## The Game

- Cogito is a single-player puzzle game. You are given a randomly shuffled board, and your goal is to rearrange the pieces to replicate the positions of the objective board as fast and with the least moves possible.
- You can do this by clicking the arrows on the borders of the board and shift collumns/rows. However the actual shift will not always be what you expect, as there are 12 different rules defining the action of the arrows, that change with each level.

### Game Rules
> There are 12 different movement rules. At the end of level 12, the game returns to the initial rule (where each movement corresponds to only the movement actually made), but increases the difficulty by changing the objective of the board.

> It is not known for sure how many different boards exist.

> At the top, there is a counter with the time of the current level, the number of the current level, the move counter for the current level, and a mysterious number.

### Movement Rules
- 1: moving a column or row corresponds to shifting the selected column or row by one
- 2: same as rule 1, but shifts 2 spaces at a time
- 3: moving a column corresponds to shifting the corresponding row and vice versa (e.g., clicking on row 1 will move column 1, etc.)
- 4: the movement is the same as the first rule, but there are fewer arrows in specific places (first and last two columns and 3 middle columns, first row, last two, and 3 middle, with rows and columns being symmetrical) (care must be taken for the initial state not to have pieces in impossible places)
- 5: same as rule 1, but the row/column moves in the opposite direction to the arrow
- 6: like in rule 5, the movement is opposite, but now it's also symmetrical (moving column n results in moving column 9-n+1)
- 7: same as previous, but in addition to moving the symmetrical column/row, it also moves the original corresponding to the arrow where clicked
- 8: moving a column/row also moves the corresponding column/row with the corresponding number. Moving right corresponds to moving up and moving left corresponds to moving down
- 9: the movement is symmetrical: moving column/row x also moves one space in column/row 9-x+1 (if moving the middle column/row, only that one is moved)
- 10: same as 8, but with arrows from 4
- 11: moving a column/row also moves the adjacent column/row. The adjacent one is considered to be to the right in the case of columns or below in the case of rows. If it's the last row/column, the additional movement will be to the first one
- 12: like 11, but instead of moving the adjacent one, it moves the column/row that is 2 to the left/down. If it goes out of the board, rule 11 applies
