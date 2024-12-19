# Ship of Fools Game

Welcome to the **Ship of Fools** game! This is a simple dice game where players compete to assemble a "Ship", "Captain", and "Crew" to score points. The first player to exceed a score of 21 wins the game.

---

## How to Play

1. **Objective**: Assemble a "Ship" (6), "Captain" (5), and "Crew" (4) using dice rolls.
2. **Setup**: Players take turns rolling 5 dice up to 3 times per round.
3. **Rules**:
   - A "Ship" must be rolled first (value 6).
   - A "Captain" can be rolled only after the "Ship" (value 5).
   - A "Crew" can be rolled only after the "Captain" (value 4).
   - Any remaining dice values after assembling the Ship, Captain, and Crew are added to the player's score.
4. **Winning**: The game continues until one player exceeds a total score of 21.

---

## Project Structure

```plaintext
.
├── ShipOfFools assignment.py   # Main implementation of the game
└── README.md                   # Project documentation
```

---

## How the Implementation Works

### 1. **Classes**

#### `Die`
- Represents a single die with values ranging from 1 to 6.
- Methods:
  - `roll()`: Rolls the die to generate a random value.
  - `get_value()`: Retrieves the current value of the die.

#### `DiceCup`
- Manages a set of 5 dice.
- Features:
  - Rolls all dice that are not "banked".
  - Tracks which dice are banked or released.
  - Methods:
    - `roll()`: Rolls unbanked dice.
    - `bank(index)`: Banks a die at a specific index.
    - `release(index)`: Releases a die at a specific index.
    - `release_all()`: Releases all dice.
    - `value(index)`: Retrieves the value of a die at a specific index.
    - `is_banked(index)`: Checks if a die is banked.

#### `ShipOfFoolsGame`
- Implements the core game logic.
- Features:
  - Rolls the dice up to 3 times per round.
  - Checks for Ship, Captain, and Crew.
  - Calculates the score based on remaining dice values after assembling the Ship, Captain, and Crew.

#### `PlayRoom`
- Manages players and game flow.
- Features:
  - Adds players to the game.
  - Tracks scores and determines when the game finishes.
  - Announces the winner.

#### `Player`
- Represents a player in the game.
- Features:
  - Tracks the player's name and score.
  - Plays a round of the game and updates the score.

---

### 2. **Gameplay Flow**

1. **Initialization**:
   - Create an instance of `PlayRoom`.
   - Set the game using `ShipOfFoolsGame`.
   - Add players to the game.

2. **Game Rounds**:
   - Players take turns rolling dice.
   - Attempt to assemble a Ship, Captain, and Crew in up to 3 rolls.
   - Scores are updated based on the remaining dice values.

3. **End Game**:
   - The first player to exceed a total score of 21 is declared the winner.

---

## Example Usage

Here's how the game is played in the script:

```python
if __name__ == "__main__":
    game_p = PlayRoom()
    game_p.set_game(ShipOfFoolsGame())
    game_p.add_player(Player("sri"))
    game_p.add_player(Player("royal"))
    game_p.add_player(Player("abhi"))

    while not game_p.game_finished():
        game_p.play_round()
        game_p.print_scores()
    game_p.print_winner()
    game_p.reset_scores()
```

---

## Key Features
- Object-oriented design with separate classes for dice, game logic, and players.
- Randomized dice rolls for a fun and unpredictable game.
- Modular structure for easy customization and expansion.

---

## How to Run the Game
1. Clone the repository or download the `ShipOfFools assignment.py` file.
2. Run the script using Python:
   ```bash
   python ShipOfFools assignment.py
   ```
3. Follow the on-screen prompts to play the game.

---

Enjoy playing **Ship of Fools** and may the best sailor win! 🚢
