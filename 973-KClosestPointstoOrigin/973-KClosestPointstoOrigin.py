# Last updated: 9/20/2026, 4:35:57 PM
1from collections import defaultdict
2import heapq
3import math
4
5class Solution:
6    """
7    first calculate the distance between points and origin, then put the distance as a key and the
8    point as a value in a hashmap, while putting a key in a minheap. then, take the min value from
9    heap and use as key and then add the points to result, keep doing this until k points are added
10    to result array and return
11    """
12    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
13        heap = []
14        hashmap = defaultdict(list)
15        
16        for point in points:
17            distance = math.sqrt(point[0]**2 + point[1]**2)
18            heappush(heap, distance)
19            hashmap[distance].append(point)
20        
21        result = list()
22        while heap:
23            curr = heappop(heap)
24            for point in hashmap[curr]:
25                if len(result) == k:
26                    return result
27                
28                result.append(point)
29        
30        return result