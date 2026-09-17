# Last updated: 9/17/2026, 3:18:15 PM
1import heapq
2
3class Solution:
4    """
5    use a maxheap; first multiply each element in piles by -1 and then create a heap, then cut the most
6    negative element in half k times, then return the total in the heap * -1 as a result.
7    """
8    def minStoneSum(self, piles: List[int], k: int) -> int:
9        for i in range(len(piles)):
10            piles[i] *= -1
11        
12        heapify(piles)
13        
14        for i in range(k):
15            curr = heappop(piles)
16            curr = curr // 2
17            heappush(piles, curr)
18        
19        result = 0
20        for i in range(len(piles)):
21            result += piles[i]
22        return result*-1