# README
You will make a game that allows the user to specify a pokemon from the video game Pokemon. They will choose between five different pokemon: Squirtle, Charmander, Bulbasaur, Pikachu, or Mewtwo. Each of these pokemon are currently at max hp (which is different for each of them) and they are trying to defeat them in a pokemon battle! They can choose from 3 different attacks and 1 healing move. They can tackle (-10 hp), scratch (-15), slam (-30), and recover (+25). To win the fight, they must bring the pokemon to exactly 0 hp. If it goes into the negatives, they accidenetally kill their friend's pokemon and will have to deal with the emotional repercussions that causes and therefore lose. They can also give up and be told that they are an utter loser and to go back home to their mom.

### Requirements:
- Squirtle has 65 hp
- Charmander has 70 hp
- Bulbasaur has 55 hp
- Pikachu has 80 hp
- Mewtwo has 500 hp
- Tackle removes 10 hp.
- Scratch removes 15 hp.
- Slam removes 30 hp.
- Recover adds 25 hp.

### The Nitty Gritty:
- The user will first be prompted to pick an opponent.
- Once an opponent is selected, they will be told their opponent's max hp and the options available to them.
- The user should **NOT** know how much hp their opponent has besides their max hp. Their indicators will be given to them when an opponent is under 50% of their health.
- They will not know how much each 'move' does.
- If the user ever picks quit, the program should call them a major loser and end.
- If the user gets the opponent to exactly 0 hp, the program should congratulate them for winning and end.
- If the user gets the opponent to a negative hp value, it should make them feel awful for killing their friends pokemon and quit.
- You should utilize dictionaries for the pokemon and their hp totals as well as the move options.
- You should have valid input validation functions that are tested and work.
- You should meet all the normal Style Guide requirements.

**Examples:** 

```
Choose an opponent Squirtle, Charmander, Bulbasaur, Pikachu, Mewtwo: Squirtle
Opponent: Squirtle
Max HP: 65
[tackle], [scratch], [slam], [recover], [run]> run
What a loser, you quit before you won. You turned around and ran home to your mom. Gross.
```
```
Choose an opponent Squirtle, Charmander, Bulbasaur, Pikachu, Mewtwo: Squirtle
Opponent: Squirtle
Max HP: 65
[tackle], [scratch], [slam], [recover], [run]> tackle
Opponent: Squirtle
Max HP: 65
[tackle], [scratch], [slam], [recover], [run]> scratch
Opponent: Squirtle
Max HP: 65
[tackle], [scratch], [slam], [recover], [run]> tackle
Squirtle is looking beat up!
Opponent: Squirtle
Current HP: 30
[tackle], [scratch], [slam], [recover], [run]> slam
Squirtle goes down! You win the battle as your friend runs to their squirtle and gives you a hearty thumbs up as they heal their Squirtle.
```
```
Choose an opponent Squirtle, Charmander, Bulbasaur, Pikachu, Mewtwo: Squirtle
Opponent: Squirtle
Max HP: 65
[tackle], [scratch], [slam], [recover], [run]> slam
Opponent: Squirtle
Max HP: 65
[tackle], [scratch], [slam], [recover], [run]> slam
OOOOOO, Squirtle is looking real real bad. 
Opponent: Squirtle
Current HP: 5
[tackle], [scratch], [slam], [recover], [run]> tackle
You watch as squirtle coughs up blood. It falls to the ground, still. You think you went to far. Your friend runs up to their pal tears streaming down their face as their pokemon wimpers. They try to heal them with a potion...but it does nothing. They look at you distraught. What did you do?!? You lose.