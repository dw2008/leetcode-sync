# Last updated: 11/1/2026, 9:20:12 PM
1from functools import cache
2
3class Solution:
4    """
5    the total amount of ways we can reach a path is the sum of all possible paths from previous steps (from up and from left). therefore, we can start at the goal and keep recursion ing back to the start point (0, 0), returning 1 as the base case (unique path found).
6    """
7    def uniquePaths(self, m: int, n: int) -> int:
8        @cache
9        def dp(i, j):
10            if i == 0 and j == 0:
11                return 1
12            paths = 0
13            if(i > 0):
14                paths += dp(i-1, j)
15            if(j > 0):
16                paths += dp(i, j-1)
17            return paths
18        
19        return dp(m-1, n-1)