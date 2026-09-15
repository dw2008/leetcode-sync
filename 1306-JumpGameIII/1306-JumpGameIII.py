# Last updated: 9/15/2026, 2:14:47 PM
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
16            print(curr_q)
17            while(curr_q):
18                curr = curr_q.popleft()
19                if(arr[curr] == 0):
20                    return True
21                visited.add(curr)
22                
23                if((curr + arr[curr]) not in visited and curr + arr[curr] < len(arr)):
24                    next_q.append(curr + arr[curr])
25                    
26                if((curr - arr[curr]) not in visited and curr - arr[curr] >= 0):
27                    next_q.append(curr - arr[curr])
28            
29            curr_q = next_q
30            next_q = deque()
31            
32        return False
33                
34                