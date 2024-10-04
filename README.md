# Hangman Game

This is a simple **Hangman Game** implemented in Python using the Pygame library.

## How to Run

1. Make sure you have Python installed on your machine.
2. Install Pygame:
    ```bash
    pip install pygame
    ```
3. Clone this repository or download the code files.

4. Run the game script:
    ```bash
    python hangman.py
    ```

## Game Instructions

- A random word will be selected from a predefined word list.
- You will have to guess letters of the word by typing on the keyboard.
- For every incorrect guess, part of the hangman is drawn.
- You lose the game if the entire hangman is drawn (6 incorrect guesses).
- Guess all the letters of the word correctly to win the game.

## File Structure

- `hangman.py`: The main game script.
- `images/`: Folder containing the hangman images for each stage of the game (from 0 to 6 wrong guesses).

## Key Features

- Random word selection from a list of programming terms.
- Visual display of correct guesses and incorrect guesses.
- Hangman drawing updated based on the number of incorrect guesses.
- Simple and interactive game loop using Pygame.

## Requirements

- Python 3.x
- Pygame

## Credits

This game was created as a fun way to demonstrate Pygame capabilities in Python. Feel free to modify and enhance it!
