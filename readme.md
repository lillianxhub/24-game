# 24 Game

This is a simple implementation of the 24 Game using Python and Tkinter for the GUI. The objective of the game is to manipulate four given numbers using basic arithmetic operations (+, -, \*, /) to achieve the result of 24.

## Features

-   Generate random sets of four numbers between 1 and 9.
-   Evaluate user-input expressions to check if they equal 24.
-   Display possible solutions if they exist.

## Requirements

-   Python 3.x
-   Tkinter (usually included with Python)

## How to Run

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the main script:
    ```sh
    python src/main.py
    ```

## How to Play

1. The game will generate a set of four random numbers.
2. Enter an arithmetic expression using these numbers to make 24.
3. Press "Check" or hit Enter to verify your expression.
4. Press "New Game" to generate a new set of numbers.
5. Press "Show Solution" to see one possible solution if you are stuck.

## Example

Given numbers: [3, 8, 3, 8]

A valid expression to make 24 could be: `(8 / (3 - (8 / 3)))`

## License

This project is licensed under the MIT License.
