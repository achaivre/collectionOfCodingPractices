# Practice 1 for Dictionaries
The purpose of this software is for the user to provide a file of people and their birtdays (month and day). That file should be converted into a dictionary where each name is paired with a birthday. The user should be able to add a birthday to the file and search a birthday from the file.

## The Brief:
- Your software should first ask a user to load a file to add birthdays to and to search from.
- Your software should convert the existing text and any other text added to the file into a dictionary that is searchable by first name, last name, or full name.
- Your user should be able to add a birthday and name to the text file. It should take the name, and birthday in one line separated by a comma.
- Your software should have valid input helpers for relevant inputs.
- Your software should be formatted with black.
- Your software should have type annotations for your functions.

## Example Execution:
-> What file do you want to load? birthdays
-> Do you want to [search] for a birthday, [add] a birthday to the file, or [quit]? search
-> Name: patrick
-> No entry found.
-> Do you want to [search] for a birthday, [add] a birthday to the file, or [quit]? add
-> Put in a person's first and last name, a comma, a space, and then the person's birth month and day. Ex: Alyx Chaivre, June 9th: > cassidy chaivre july 6th
-> Invalid entry.
-> Put in a person's first and last name, a comma, a space, and then the person's birth month and day. Ex: Alyx Chaivre, June 9th: > cassidy chaivre, july 6th
-> Do you want to [search] for a birthday, [add] a birthday to the file, or [quit]? search
-> Name: cassidy
-> Cassidy Chaivre's birthday is July 6th.
-> Do you want to [search] for a birthday, [add] a birthday to the file, or [quit]? quit

## Text File Execution:
-> Alyx Chaivre, June 9th
-> Cassidy Chaivre, July 6th

## Extra Challenge:
If you want a bit of an extra challenge/added piece, you can have your software check when it needs to add the 's to the end of a name. For example, Greyson Williams has an s at the end so we wouldn't grammatically have it put Greyson Williams's, we'd have it put Greyson Williams' in the search.