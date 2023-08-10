# from typing import Tuple

# game_list = Tuple[str, str, float, float, float, bool]
# favorite = ['favorite','not favorite']

def filter_by_console(games: list, user_console: str) -> list:
 ...
  
def filter_by_duration(games: list, number: float) -> list:
  ...
 
def filter_by_players(games:list, players: int) -> list:
  ...

def filter_by_rating(games: list, number: float) -> list:
...
      
def filter_by_favorite(games: list) -> list:
  ...


# ========== FILL IN CODE ABOVE ====================
# ========== DO NOT TOUCH CODE BELOW ===============

games = [('Mario Party', 'Nintendo', 12.2, 3.2, 4, True), ('Call of Duty', 'Xbox', 62.3, 2.4, 2, True), ('Elden Ring','PS', 112.3, 3.9, 1, False), ('Ark', 'PC', 432.4, 2.7, 1, False), ('Apex Legends', 'PS', 42, 3.1, 1, False), ('Madden', 'Xbox', 22.4, 1.4, 2, False), ('NBA 2k', 'Xbox', 5.2, 1.9, 4, True), ('Legend of Zelda', 'Nintendo', 73.4, 3.6, 1, True), ('Civilization 5', 'PC', 174.2, 2.7, 1, False), ('Zoo Tycoon', 'PC', 7.3, 2.1, 1, True), ('Spider Man', 'PS', 34.2, 3.0, 1, False), ('Among Us', 'PC', 15.6, 2.1, 8, False), ('Mario Kart', 'Nintendo', 13.2, 2.8, 4, False), ('Stardew Valley', 'PC', 922.3, 3.7, 4, True)]

def inputhelper_float() -> float:
  while True:
    user = input('Value: ')
    try:
      user = float(user)
      if user > 0:
        return user
    except ValueError:
      print('Invalid input.')

def inputhelper_user() -> str:
  commands = ['console', 'duration', 'players', 'rating', 'favorite', 'quit']
  user = input('Filter the games by [console], [duration], [players], [rating], [favorite], or [quit]').lower()
  while user not in commands:
    print('invalid action.')
    user = input('Filter the games by [console], [duration], [players], [rating], [favorite], or [quit]').lower()
  return user

def inputhelper_console() -> str:
  commands = ['nintendo', 'xbox', 'ps', 'pc']
  user = input('By what console: ').lower()
  while user not in commands:
    print('invalid entry.')
    user = input('By what console: ').lower()
  return user

def main():
  while True:
    user = inputhelper_user()
    if user == 'console':
      user_console = inputhelper_console()
      consoles_filter = filter_by_console(games, user_console)
      for game in consoles_filter:
        print(game)
    elif user == 'duration':
      number = inputhelper_float()
      duration_filter = filter_by_duration(games, number)
      for game in duration_filter:
        print(game)
    elif user == 'players':
      number = inputhelper_float()
      players_filter = filter_by_players(games, number)
      for game in players_filter:
        print(game)
    elif user == 'rating':
      number = inputhelper_float()
      rating_filter = filter_by_rating(games, number)
      for game in rating_filter:
        print(game)
    elif user == 'favorite':
      favorite_filter = filter_by_favorite(games)
      for game in favorite_filter:
        print(game)
    elif user == 'quit':
      break

main()