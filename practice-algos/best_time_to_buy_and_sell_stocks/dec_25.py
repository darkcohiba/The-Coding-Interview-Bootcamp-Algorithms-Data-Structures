def maxProfit(stocks):
    max_profit = 0
    min_price = stocks[0]
    for stock in stocks:
        if stock < min_price:
            min_price = stock
        elif 

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([2,1,5,2,6,4]))
print(maxProfit([4,1,3,3,6,4]))