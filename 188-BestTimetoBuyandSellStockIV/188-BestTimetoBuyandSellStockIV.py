# Last updated: 10/26/2026, 9:11:57 PM
1from functools import cache
2
3class Solution:
4    """
5    we can keep track of a few variables: current index, currently holding stock (boolean), and remaining actions. for each day, we can choose either to buy, sell, or skip. if we buy, then we subtract the current price of stock and move on with holding=true, remaining. if we sell, we add the current price of stock and move on with holding=false, remaining-1. if we skip, we move on with holding the same and remaining the same. we can take the maximum of these three actions for each day, assuming we are able to perform them.
6    """
7    def maxProfit(self, k: int, prices: list[int]) -> int:
8        @cache
9        def dp(i, holding, remaining):
10            if(i == len(prices) or remaining == 0):
11                return 0
12
13            if(holding):
14                return max(dp(i+1, False, remaining-1) + prices[i], dp(i+1, True, remaining))
15            else:
16                return max(dp(i+1, True, remaining) - prices[i], dp(i+1, False, remaining))
17        
18        return dp(0, False, k)
19            