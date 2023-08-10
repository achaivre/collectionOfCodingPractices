# Practice 1
## Brief:
[ You will be making a betting dice game.]

### Rubric:
- You should use a dataclass, 'Game'.
- You should have proper input validation functions.
- You should have at least two functions besides main.
- All functions should be properly tested and have type annotations.
- A player should start with 100 coins.
- The game ends when player quits or when they are out of coins (0 or less).
    - If the player is out of coins, the game should end and say "Better luck next time!"
    - If they quit, the player should be told 'No one should walk away from a table when they are up ;)'
- While the game is running, the player should be prompted to make a bet. They cannot make a bet more than the amount of current coins they have.
- Once the bet is done, the program should roll 2 six sided die (Number generator 2 - 12).
    - If a user rolls a 7, they should get double what they bet.
    - If a user rolls above a 7, they should get coins equal to their bet.
    - if a user rolls 6 or below, they should lose coins equal to their bet.
    - If a user rolls 2 (snake eyes), they should lose coins equal to double the amount equal to their bet. 