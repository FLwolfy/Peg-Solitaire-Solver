# Peg-Solitaire-Solver
Welcome to Peg Solitair Solver. This is a really simple way to solve English Peg Solitaire problems.

## Overview
This project explores a simple solution to the English Peg-Solitaire puzzle. The primary method involves using a recursive backtracking approach to handle the game board. Memorization is employed to store previously explored states, reducing computational overhead. To expedite the search for possible solutions, the recursive approach prioritizes moving the current peg along the longest possible path before considering other pegs. This strategy aims to get rid of unnecessary performance costs.

## Usage
1. **Download Source Code:**
   Clone or download the source code from the repository.

2. **Create Boards**
   Create your own boards or use the example board in the `Board.py` file. Here is the template:
   ```python
   boardTemplate = """\
     XXX  
     XXX  
   XXXXXXX
   XXXXXXX
   XXXXXXX
     XXX
     XXX  
   """
   ```

3. **Run Solver:**
   Execute the following code in the `Main.py` file:
   
    **Get steps (fromRow, fromCol, toRow, toCol) as a list**
    ```python
    steps = PegSolitaire.solve(board)
    ```
   
    **Check runtime**
    ```python
    PegSolitaire.solve_test(board)
    ```
   
    **Visualize step-by-step process**
    ```python
    PegSolitaire.show_steps(board)
    ```

## Notes
This method is a personal learning project summary, and its efficiency is not optimal. There is substantial room for optimization, and discussions and contributions are welcome.
