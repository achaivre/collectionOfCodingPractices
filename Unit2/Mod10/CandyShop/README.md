# README
The purpose of this software is to create a pos system for a candy store! This candy store has two different selling options. You can purchase a candy by weight or by a set amount of money. Your software will prompt the user to choose whether they are purchasing a candy by weight or by a set dollar amount and then will choose which candy they would like to purchase, give the user an option to purchase another candy or to finish their sale and at the end have it print the receipt in the console.

### The Nitty Gritty:
- Your software will convert a provided text file of candy prices and candy into a searchable dictionary.
- Your software will allow the cashier to choose between purchasing a candy by weight or by a set amount of money.
- Your software will allow the cahsier to choose the candy they would like to purchase.
- It will prompt the user to purchase another candy or be done with their purchase.
- When they are finished, it will print a receipt that itemizes all the things purchased, the amount, and how much they spent total.
- All inputs should have valid input validation functions.
- Your main should be implemented in a if __name__ == '__main__':
- Your units should print out as a float.

### Example Console:
- Welcome to the Candy Shop!
- We won't let you lick any lollipops before you purchase them though!
- Please load the file with all available candies and their price per unit: candy_prices
- The candies available for purchase are:
  - Lollipops --- $1.00
  - Gumdrops --- $1.50
  - Chocolate --- $1.75
  - Gummies --- $2.50
- Candy: guMMies
- By weight or by dollar: dollar
- Amount Spent: -10
- Please put in a valid dollar amount.
- Amount Spent: 10
- Another candy [yes] or [no]: yes
- Candy: lOlli-pops
- Please put in a valid candy.
- Candy: lollipops
- By weight or by dollar: weight
- Weight of Candy: 5
- Another candy [yes] or [no]: no
- Here is your receipt:
  - Gummies - $2.50 - 4.0 units - Total: $10.00
  - Lollipops - $1.00 - 5.0 units - Total: $5.00
- Your total is $15.00

### Example txt file to load:
- Gumdrops, 1.50
- Gummies, 2.50
- Lollipops, 1.00
- Chocolate, 1.75