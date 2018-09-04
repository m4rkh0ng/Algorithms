# Stock Prices

You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock. 

Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices.

###### MH: Why is this not 3792 instead of 3530? What about that 3800 - 2? Why are we looking at 3800 - 270 for the maximum profit?

## Testing

Run the test file by executing `python test_stock_prices.py`.

You can also test your implementation manually by executing `python stock_prices.py [integers_separated_by_a_single_space]`

## Hints

 * For this problem, we essentially want to find the difference between the smallest and largest prices in the list of prices.

 ###### MH: ^ if this is the case, and we're not told from the beginning how much our starting capital is, then I disagree with the implemented solutions/tests because of the nature of the question. Please inform me, though, of how to view this differently to understand what the question is asking for. If we're meant to be reading the list of stock prices in chronological order, then that could stand to be stated more clearly instead of "difference between the smallest and largest prices in the list of prices" because then, I'm looking at it as a list of integers instead of a graph of price change over time in one direction.