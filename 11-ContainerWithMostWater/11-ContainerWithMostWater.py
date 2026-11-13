# Last updated: 11/12/2026, 9:03:49 PM
1class Solution:
2    """
3    sliding window: we can set the window as the whole container (1 pointer to the start, 1 pointer to the end). we can calculate the area for each container and store the maximum, and move the smaller line pointer to the center until they converge.
4    """
5    def maxArea(self, height: list[int]) -> int:
6        left = 0
7        right = len(height) - 1
8        res = float('-inf')
9        while(left < right):
10            curr = (right - left) * min(height[right], height[left])
11            res = max(curr, res)
12            if(height[right] > height[left]):
13                left += 1
14            else:
15                right -= 1
16        return res