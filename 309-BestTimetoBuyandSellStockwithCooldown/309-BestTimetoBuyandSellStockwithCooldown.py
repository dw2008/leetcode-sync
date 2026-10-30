# Last updated: 10/30/2026, 4:44:34 PM
1from functools import cache
2
3class Solution:
4    """
5    more dp!! just keep track of a cooldown thing as well on top of the other stuff
6    """
7    def maxProfit(self, prices: list[int]) -> int:
8        @cache
9        def dp(index, holding, cooldown):
10            if index >= len(prices):
11                return 0
12            if(cooldown):
13                return dp(index+1, False, False)
14            if(holding):
15                return max(dp(index+1, False, True) + prices[index], dp(index+1, True, False))
16            return max(dp(index+1, True, False) - prices[index], dp(index+1, False, False))
17        
18        return dp(0, False, False)