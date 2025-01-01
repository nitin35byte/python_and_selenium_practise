def max_profit(prices):
    n = len(prices)
    # if n <= 1:
    #     return 0

    profit = 0
    for i in range(1, n):
        if prices[i] >prices[i-1]:
            profit +=prices[i] - prices[i-1]
    return profit


prices1 = [7,1,5,3,6,4]
print(max_profit(prices1))  # Output: 7

# Test Example 2
prices2 = [1,2,3,4,5]
print(max_profit(prices2))  # Output: 4