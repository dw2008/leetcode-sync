# Last updated: 11/2/2026, 3:55:07 PM
1from functools import cache
2
3class Solution:
4    """
5    dp: start at the bottom right. then, we can recursively take the minimum path to that point and the point before that, etc. we can cache and take the base case as the top left node.
6    """
7    def minPathSum(self, grid: list[list[int]]) -> int:
8        @cache
9        def dp(row, col):
10            if row == 0 and col == 0:
11                return grid[0][0]
12            minpath = float('inf')
13            if row > 0:
14                minpath = min(dp(row-1, col), minpath)
15            if col > 0:
16                minpath = min(dp(row, col-1), minpath)
17            return minpath + grid[row][col]
18        
19        return dp(len(grid)-1, len(grid[0])-1)