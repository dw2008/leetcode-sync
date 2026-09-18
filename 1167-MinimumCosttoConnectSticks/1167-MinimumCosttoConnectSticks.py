# Last updated: 9/18/2026, 5:16:57 PM
1import heapq
2
3class Solution:
4    """
5    from the examples, it appears that the smallest cost will be to combine the two smallest sticks
6    (makes sense, because the initial costs are added in to later costs so you want the smallest costs
7    first). therefore, while there is more than one stick, use a min heap to find the smallest two 
8    sticks, combine them, add them to a cost tracker, and return the cost tracker.
9    """
10    def connectSticks(self, sticks: list[int]) -> int:
11        heapify(sticks)
12        cost = 0
13        
14        while(len(sticks) > 1):
15            one = heappop(sticks)
16            two = heappop(sticks)
17            cost += (one + two)
18            heappush(sticks, one + two)
19        
20        return cost