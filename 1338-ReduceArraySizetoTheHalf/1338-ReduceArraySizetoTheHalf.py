# Last updated: 9/25/2026, 4:50:27 PM
1from collections import defaultdict
2
3class Solution:
4    """
5    First make a counter with the number of times a number is seen in the array. then, sort the hashmap by value (decreasing), then keep choosing
6    the largest value and incrementing a running sum, while adding 1 to a counter. return counter once
7    the running sum is greater than or equal to half the array size.
8    """
9    def minSetSize(self, arr: list[int]) -> int:
10        hash1 = defaultdict(int)
11        for n in arr:
12            hash1[n] = hash1[n] + 1
13        
14        counter = 0
15        totalSum = 0
16        hash2 = {k: v for k, v in sorted(hash1.items(), key=lambda item: item[1], reverse=True)}
17        
18        for key, value in hash2.items():
19            totalSum += value
20            counter += 1
21            
22            if(totalSum >= len(arr)/2):
23                return counter
24            
25        return counter