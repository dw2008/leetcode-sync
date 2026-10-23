# Last updated: 10/23/2026, 3:38:24 PM
1from functools import lru_cache
2
3class Solution:
4    """
5    use dp, since hte problem can be divided into subtrees we can cache former results and then backtrack to cut partial solutions in the tree and calculate solutions based on each denomination of coin and what would happen if we took one of that denomination (while backtracking each step), base case is if the coin value goes over the limit
6    """
7    def coinChange(self, coins: list[int], amount: int) -> int:
8        @lru_cache(None)
9        def dp(remainder):
10            if(remainder < 0):
11                return -1
12            if(remainder == 0):
13                return 0
14            min_cost = float('inf')
15            for coin in coins:
16                result = dp(remainder - coin)
17                if(result != -1):
18                    min_cost = min(min_cost, result + 1)
19            if(min_cost != float('inf')):
20                return min_cost
21            return -1
22        
23        return dp(amount)
24                