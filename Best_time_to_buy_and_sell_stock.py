def maxProfit(prices):
    minPrice = float('inf')
    maxPrice = 0
    for price in prices:
        if price < minPrice:
            minPrice = price

        profit = price - minPrice

        if profit > maxPrice:
            maxPrice = profit
    return maxPrice
prices = [7, 1, 5, 3, 6, 4]  
print(maxProfit(prices))          