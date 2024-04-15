# AI Game Project

This project was developed as part of a course on artificial intelligence for games during the fourth year at INSA Rennes. The aim of this project is to implement an AI agent capable of playing a game of ultimate tic tac toe.

## Setup
To use the program, follow these steps:

1. Make sure you have Python 3 installed on your system.
2. Modify the parameters in `parameters.txt` according to your preferences:
   - `Depth`: Set to either 2 or 3 to adjust the level of depth of the game. (it's not really playable agains AI in depth 3)
   - `Nb game`: Specify the number of games to play.
   - `Display game`: Set to either `True` or `False` to indicate whether to display the game or not.
3. Run the program using the following command:
   ```
   python3 main.py <depth> <nb_game> <display_game>
   ```
   Replace `<depth>`, `<nb_game>`, and `<display_game>` with appropriate values.
4. Interact with the program using the following controls:
   - Press `Space` to make it play by itself.
   - Press `Arrow Up` to make it play only one turn.

   