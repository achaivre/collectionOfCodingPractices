# README
### The brief:
You will be creating a software that allows users to type in their products, a description, and their price. Then they will be able to input when a user buys a product to track which product they have is the most popular. When the program ends, it should print out which product sold the best and which sold the worst.

### Rubric:
1. Products should be created and added to a list using a dataclass called Product and taking multiple relevant fields.
2. The users should be asked [Product?] or [Done?] at the beginning of the program.
3. If product is picked, the user should be asked to input the product name, a description, and the unit price.
4. If they choose done, the user should then be asked [Which product was purchased, product look up, or done?]
5. If they choose which was purchased, they should be asked the product name, and the total number of that product purchased should go up by one.
6. If they choose product look up, it should look up a product by name and then print to the console the description, the unit price, and how much has been bought so far.
7. If they select done, the program should end and it should print out to the console which product had the most units sold, for a total of what price, and which product had the least units sold, for a total of what price.
8. You do not need to worry about what happens if a tie occurs.

### Example Console:
- Welcome to the Product Purchase Tracker.
- Please select [product] entry or [done]: proDUCt
- Product Name: Tic Tacs
- Product Desc: White pills that make breath smell good good.
- Unit Price: 2.0
- Please select [product] entry or [done]: PrOdUcT
- Product Name: Twix
- Product Desc: Right or Left, amirite?
- Unit Price: 1.50
- Please select [product] entry or [done]: prOduct
- Product Name: Dasani Water
- Product Desc: Water....expensive.
- Unit Price: 3
- Please select [product] entry or [done]: dONe
- Would you like to [tally] a purchase of a product, [lookup] a product, or are you [done]? tally
- Product Name: Tic Tacs
- Would you like to [tally] a purchase of a product, [lookup] a product, or are you [done]? tally
- Product Name: Twix
- Would you like to [tally] a purchase of a product, [lookup] a product, or are you [done]? lookup
- Product Name: Tic Tacs
- Product Desc: White pills that make breath smell good good.
- Unit Price: 2.0
- Number Sold: 1
- Would you like to [tally] a purchase of a product, [lookup] a product, or are you [done]? taLLy
- Product Name: tic tacs
- Would you like to [tally] a purchase of a product, [lookup] a product, or are you [done]? Tally
- Product Name: Dasani waTer
- Would you like to [tally] a purchase of a product, [lookup] a product, or are you [done]? tallY
- Product Name: twIx
- Would you like to [tally] a purchase of a product, [lookup] a product, or are you [done]? tally
- Product Name: Lays
- Product does not exist.
- Would you like to [tally] a purchase of a product, [lookup] a product, or are you [done]? talttttty
- Invalid action.
- Would you like to [tally] a purchase of a product, [lookup] a product, or are you [done]? TaLLy
- TiC TaCS
- Would you like to [tally] a purchase of a product, [lookup] a product, or are you [done]? DONE
- The product sold the most was Tic Tacs with 3 units sold.
- The product sold the least was Dasani Water with 1 unit sold.
