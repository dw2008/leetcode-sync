# Last updated: 9/25/2026, 4:48:21 PM
1from collections import defaultdict
2
3class Solution:
4    """
5    first iterate through the array and add numbers to a hashmap with the number as the key and the
6    number of occurences as its value, incrementing the number of occurences by one for every time
7    the number is found in the array. then, sort the hashmap by value (decreasing), then keep choosing
8    the largest value and incrementing a running sum, while adding 1 to a counter. return counter once
9    the running sum is greater than or equal to half the array size.
10    """
11    def minSetSize(self, arr: list[int]) -> int:
12        hash1 = defaultdict(int)
13        for n in arr:
14            hash1[n] = hash1[n] + 1
15        
16        counter = 0
17        totalSum = 0
18        hash2 = {k: v for k, v in sorted(hash1.items(), key=lambda item: item[1], reverse=True)}
19        print(hash2)
20        
21        for key, value in hash2.items():
22            totalSum += value
23            counter += 1
24            
25            if(totalSum >= len(arr)/2):
26                return counter
27            
28        return counter