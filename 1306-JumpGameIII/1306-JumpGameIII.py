# Last updated: 9/15/2026, 2:14:54 PM
1from collections import deque
2
3class Solution:
4    """
5    use bfs starting at start index, treat each index having max of 2 neighbors: arr[i-arr[i]] and 
6    arr[i+arr[i]]; return true if a 0 value is reached. keep track of visited nodes and also use
7    2 queues
8    """
9    def canReach(self, arr: List[int], start: int) -> bool:
10        visited = set()
11        curr_q = deque()
12        next_q = deque()
13        curr_q.append(start)
14        
15        while(curr_q):
16            while(curr_q):
17                curr = curr_q.popleft()
18                if(arr[curr] == 0):
19                    return True
20                visited.add(curr)
21                
22                if((curr + arr[curr]) not in visited and curr + arr[curr] < len(arr)):
23                    next_q.append(curr + arr[curr])
24                    
25                if((curr - arr[curr]) not in visited and curr - arr[curr] >= 0):
26                    next_q.append(curr - arr[curr])
27            
28            curr_q = next_q
29            next_q = deque()
30            
31        return False
32                
33                