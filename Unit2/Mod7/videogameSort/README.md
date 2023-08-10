# README
## Brief:
Your task is to complete/implement a few functions that will return a list of Tuples. Each tuple in this list represents a video game. The tuple is broken up as follows (Name of Game(str), Which Console(str), Avg. Duration in hours(float), Avg. Rating(float), Number of Max Players(int), Favorite(Bool)).



You will be implementing the following functions:

- filter_by_console(games: list) -> list:
    - This should filter a list of games (tuples) by the selected console type (PS, Xbox, Nintendo, PC) and return a list of just the games that are on that console type.
    - 
- filter_by_duration(games: list) -> list:
    - This should filter a list of games (tuples) by returning a list of games under the chosen duration (12.2 hours, 60.9 hours, etc).
    - 
- filter_by_players(games: list) -> list:
    - This should filter games that allow you to play with chosen number of players and return a list of them (if the user puts in 2, it should return a list of all games that allow 2 players).
    - 
- filter_by_rating(games: list) -> list:
    - This should filter games by average rating (a user should be able to put a value between 0.5 and 4) and have all games with a higher than the value given rating return in a list.
    - 
- filter_by_favorite(games: list) -> list:
    - This should filter games by whether or not they are a favorite and return a list of the games that are considered favorites.