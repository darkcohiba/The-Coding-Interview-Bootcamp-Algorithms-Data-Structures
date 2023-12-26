def maxProfit(stocks):
    max_profit = 0
    min_price = stocks[0]
    for stock in stocks:
        if stock < min_price:
            min_price = stock
        # first number is 7, the stock will not be greater
        elif stock - min_price > max_profit:
            max_profit = stock - min_price
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([2,1,5,2,6,4]))
print(maxProfit([4,1,3,3,3,4]))