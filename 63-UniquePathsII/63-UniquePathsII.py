# Last updated: 11/3/2026, 1:21:09 PM
1from functools import cache
2
3class Solution:
4    """
5    DP: starting from the end, from each point of the grid, take the number of possible paths to reach that point (from top or left). if the space is an obstacle, do not dp recurse through that space. if you reach the start, add 1 to the possible paths. edge case where end is an obstacle or start is an obstacle = fail
6    """
7    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
8        @cache
9        def dp(row, col):
10            if row == 0 and col == 0:
11                return 1
12            paths = 0
13            if row > 0 and obstacleGrid[row-1][col] == 0:
14                paths += dp(row-1, col)
15            if col > 0 and obstacleGrid[row][col-1] == 0:
16                paths += dp(row, col-1)
17            
18            return paths
19        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1:
20            return 0
21        return dp(len(obstacleGrid)-1, len(obstacleGrid[0])-1)