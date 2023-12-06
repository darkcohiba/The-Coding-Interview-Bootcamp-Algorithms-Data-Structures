from typing import List

def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([2,1,5,2,6,4]))
print(maxProfit([4,1,3,3,6,4]))