# Last updated: 9/24/2026, 7:41:31 PM
1class Solution:
2    """
3    sort the array and then use greedy approach of adding smallest apples first until the basket is
4    at the maximum weight, then return max weight
5    """
6    def maxNumberOfApples(self, weight: list[int]) -> int:
7        weight.sort()
8        curr = 0
9        
10        for i in range(len(weight)):
11            curr += weight[i]
12            print(curr)
13            if(curr == 5000):
14                return i + 1
15            if(curr > 5000):
16                return i
17        
18        return len(weight)