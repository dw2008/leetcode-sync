# Last updated: 11/4/2026, 3:47:34 PM
1from functools import cache
2
3class Solution:
4    """
5    we can use dp to check the smallest falling path to any of the bottom row. we can then take the minimum of those falling paths, and return that minimum.
6    """
7    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
8        @cache
9        def dp(row, col):
10            if row < 0:
11                return 0
12            min_path = float('inf')
13            if col > 0:
14                min_path = min(min_path, dp(row-1,col-1))
15            if col < len(matrix[0]) -1:
16                min_path = min(min_path, dp(row-1, col+1))
17            min_path = min(min_path, dp(row-1, col))
18            return min_path + matrix[row][col]
19        
20        final_min = float('inf')
21        for i in range(0, len(matrix[0])):
22            final_min = min(final_min, dp(len(matrix)-1, i))
23        
24        return final_min