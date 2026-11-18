# Last updated: 11/18/2026, 5:36:07 PM
1class Solution:
2    """
3    we can first find the position to insert the newInterval using a binary search and inserting it into intervals. afterwards, we can move each interval over to a new result array and merge any intervals that have a starting interval that is smaller or equal to than the last inserted interval's ending interval. 
4    """
5    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
6        if not intervals:
7            return [newInterval]
8        
9        left = 0
10        right = len(intervals)-1
11        start = newInterval[0]
12
13        while(left <= right):
14            mid = (left+right)//2
15            if(intervals[mid][0] < start):
16                left = mid+1
17            else:
18                right = mid-1
19        
20        intervals.insert(left, newInterval)
21
22        res = []
23        for interval in intervals:
24            if not res or res[-1][1] < interval[0]:
25                res.append(interval)
26            else:
27                res[-1][1] = max(res[-1][1], interval[1])
28        
29        return res