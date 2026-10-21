# Last updated: 10/21/2026, 3:44:37 PM
1from functools import cache
2
3class Solution:
4    """
5    using dp: memoize the amount of ways you can climb to a stair, and for future stairs, memoize those by making the ways to climb add up from the n-1 and n-2 stair's ways. then, return the top step.
6    """
7    def climbStairs(self, n: int) -> int:
8        @cache
9        def dp(i):
10            if(i == 0):
11                return 1
12            if(i == 1):
13                return 2
14            return dp(i - 1) + dp(i - 2)
15        
16        return dp(n-1)
17            