# Last updated: 9/26/2026, 5:15:50 PM
1class Solution:
2    """
3    just do binary search but return the position where left >= right if not found ig
4    """
5    def searchInsert(self, nums: list[int], target: int) -> int:
6        left = 0
7        right = len(nums)-1
8        
9        while left <= right:
10            mid = (left + right)//2
11            
12            if nums[mid] == target:
13                return mid
14            
15            elif(nums[mid]) > target:
16                right = mid - 1
17            
18            else:
19                left = mid + 1
20        
21        return left