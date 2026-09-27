# Last updated: 9/27/2026, 4:14:06 PM
1class Solution:
2    """
3    first create a prefix sum array of nums sorted. then for each query, find the index that it would
4    be inserted into the prefix array at using binary search, and put that index + 1 as its maximum 
5    sum. then return array of all the maximum sums.
6    """
7    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
8        nums.sort()
9        prefix = [nums[0]]
10        
11        for i in range(1, len(nums)):
12            prefix.append(prefix[i - 1] + nums[i])
13        
14        result = list()
15        for q in queries:
16            left = 0
17            right = len(prefix) - 1
18            index = -1
19            
20            while(left <= right):
21                mid = (left + right)//2
22                
23                if(prefix[mid] == q):
24                    index = mid
25                    break
26                
27                elif(prefix[mid] > q):
28                    right = mid - 1
29                
30                else:
31                    left = mid + 1
32                
33            if(index == -1):
34                index = (left + right)//2
35            
36            result.append(index + 1)
37        
38        return result