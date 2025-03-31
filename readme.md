# Snake Game

## Overview

A classic Snake game built with Python and Tkinter. Control a snake as it moves around the screen, eating food and growing longer. The game features a customizable speed setting, pause functionality, and an intuitive user interface.

## Features

- Adjustable game speed via slider control
- Pause/resume gameplay with 'P' key
- Score tracking
- Game over screen with restart options
- Clean, modern user interface

## Requirements

- Python 3.x
- Tkinter (included with standard Python installation)

## How to Play

1. Run the game:
   ```sh
   python snake_v2.py
   ```
2. Use the slider to set your preferred game speed.
3. Click "Start Game" to begin.
4. Control the snake using arrow keys:
   - **↑ (Up Arrow)**: Move up
   - **↓ (Down Arrow)**: Move down
   - **← (Left Arrow)**: Move left
   - **→ (Right Arrow)**: Move right
5. Press 'P' to pause/resume the game.
6. Eat food (red squares) to grow and increase your score.
7. Avoid hitting the walls or the snake's own body.

## Game Rules

- The snake moves continuously in the direction of the last arrow key pressed.
- Each piece of food eaten increases your score by 1 point.
- The snake grows longer each time it eats food.
- The game ends if the snake hits a wall or itself.
- You cannot reverse direction (e.g., if moving right, you cannot immediately move left).

## Tips

- Start with a slower speed until you get comfortable with the controls.
- Plan your moves in advance, especially as the snake grows longer.
- Create a strategy to maximize the available space.

## Credits

Created by **@flowstxte**
