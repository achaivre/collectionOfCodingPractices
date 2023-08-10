# README
### The Brief
You will be making a highscore recording software for an arcade. Where you will be given a text file with a list of initials called `high_scorers.txt`. Your software should make a txt file for each high_scorer from a user provided txt file and name it the `initials_highscore.txt`. Then you should prompt the user to give the date they achieved their highscore (month day and year), what their highscore was numerically, and on which game.

### The nitty gritty:
+ Your code should do the following things:
+   + Take a user input for a provided txt file of initials of highscorers.
    + Create a file for each of the provided initials that is named the *initials_highscore.txt* that stores the following information each on their own line:
    +   + Date of highscore which includes valid month, valid day, and a valid year (1975 - Present). This input should be taken in one line and validated for all of it's elements.
        + The game they achieved the highscore on.
        + A valid integer highscore (1 - any other positive value)

### File Appearance for AMC_highscore.txt:
> - March 30 1999
> - Tetris
> - 10
---



### Console:
> + File Name: high_scorers.txt
> + AMC
> + Date of highscore: March 40 1999
> + Date is invalid
> + Date of highscore: March 30 1999
> + Game: Tetris
> + Score: afjkd;ajdf
> + Score is invalid
> + Score: 10
> + JER
> + Date of highscore: ...
> + **Note: It should run through the code above until it has run through all the initials in the user provided txt file.**


### Style Guide:
> - Code should be formatted with black.
> - Input helper functions should be defined at the top of the file.
> - Date, Score, and Inputting the file name should all have valid and working input validations.
> - There should not be any unnecessary commented out code.
> - All functions should have type annotations.