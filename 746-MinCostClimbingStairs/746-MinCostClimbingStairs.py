# Last updated: 10/22/2026, 9:11:26 PM
1class Solution:
2    """
3    using DP: since we know at each step we had to arrive from the previous or the one before the previous stair, we can add that cost into the cost of climbing onto the current step. we can also ekep track of old costs in an array so we can access those for more efficiency.
4    """
5    def minCostClimbingStairs(self, cost: list[int]) -> int:
6        memo = {} #empty dict
7        def dp(i):
8            if(i <= 1):
9                return 0 #starting at this step
10            if(i in memo):
11                return memo[i]
12            memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
13            return memo[i]
14
15        return dp(len(cost))