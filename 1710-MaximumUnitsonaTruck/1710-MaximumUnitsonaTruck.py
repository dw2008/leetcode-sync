# Last updated: 9/23/2026, 2:29:15 PM
1import heapq
2from collections import defaultdict
3
4class Solution:
5    """
6    greedy approach: first put each key/value in a hashmap (key = number of units per box, value = # of 
7    boxes) putting each key in a max heap. then go
8    through the heap and keep putting as many of the boxes with the most units as you can until the 
9    truck is full.
10    """
11    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
12        hashmap = defaultdict(int)
13        heap = list()
14        
15        for i in range(len(boxTypes)):
16            heappush(heap, boxTypes[i][1]*-1)
17            hashmap[boxTypes[i][1]]
18            hashmap[boxTypes[i][1]] = hashmap[boxTypes[i][1]] + boxTypes[i][0]
19        
20        units = 0
21        while(truckSize > 0 and heap):
22            curr = heappop(heap) * -1
23            while(truckSize > 0 and hashmap[curr] > 0):
24                truckSize -= 1
25                hashmap[curr] -= 1
26                units += curr
27        
28        return units