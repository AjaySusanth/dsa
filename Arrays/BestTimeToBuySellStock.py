'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''

def optimal(prices):
    mini = prices[0]
    profit = 0 # Min profit zero, buy and sell on same day
    for i in range(len(prices)):
        cost = prices[i] - mini
        profit = max(profit,cost)
        mini = min(prices[i],mini)

    return profit

prices = [7,1,5,3,6,4]
print(optimal(prices))