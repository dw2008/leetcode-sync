# Last updated: 9/25/2026, 4:52:04 PM
1from collections import defaultdict
2
3class Solution:
4    """
5    First make a counter with the number of times a number is seen in the array. then, sort the hashmap by value (decreasing), then keep choosing
6    the largest value and incrementing a running sum, while adding 1 to a counter. return counter once
7    the running sum is greater than or equal to half the array size.
8    """
9    def minSetSize(self, arr: list[int]) -> int:
10        counts = collections.Counter(arr)
11        counts = [count for number, count in counts.most_common()]
12        
13        total_removed = 0
14        counter = 0
15        for count in counts:
16            total_removed += count
17            counter += 1
18            if(total_removed >= len(arr)//2):
19                break
20        
21        return counter