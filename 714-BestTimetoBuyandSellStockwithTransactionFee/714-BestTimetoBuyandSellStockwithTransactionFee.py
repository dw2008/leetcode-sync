# Last updated: 10/29/2026, 2:49:18 PM
1from functools import cache
2
3class Solution:
4    """
5    for each position, try each possible action given buy/sell/hold and take the maximum of that dp function. we can pass in the current index and whether we are holding and jsut keep track of those two parameters. if we are holding, we can take the max of selling now or holding, subtracting the fee. if we are not holding, we can take the max of buying now or skipping.
6    """
7    def maxProfit(self, prices: list[int], fee: int) -> int:
8        @cache
9        def dp(index, holding):
10            if index >= len(prices):
11                return 0
12            if holding:
13                return max(dp(index+1, False) + prices[index] - fee, dp(index+1, True))
14            else:
15                return max(dp(index+1, True) - prices[index], dp(index+1, False))
16        
17        return dp(0, False)