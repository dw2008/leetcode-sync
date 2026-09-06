# Last updated: 9/5/2026, 8:48:53 PM
1from collections import deque
2
3class Solution:
4    """
5    start bfs ing from the entrance and just keep track of visited nodes in a set to not visit again,
6    probably no need to even put things in a dictionary cause can just bfs directly; also in order
7    to keep track of the count keep a current queue and a next queue; when adding neighbors add to
8    the next queue and then when current queue is empty add 1 to count and then set current queue
9    to next queue; if both queues are empty then return -1
10    """
11    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
12        visited = set()
13        currQueue = deque()
14        nextQueue = deque()
15        currQueue.append((entrance[0], entrance[1]))
16        count = 0
17        
18        while(currQueue or nextQueue):
19            while(currQueue):
20                coord = currQueue.popleft()
21                if(coord in visited):
22                    continue
23
24                visited.add(coord)
25                i = coord[0]
26                j = coord[1]
27                
28                if(count > 0 and (i == 0 or i == len(maze) - 1 
29                                  or j == 0 or j == len(maze[0]) - 1)):
30                    return count
31
32                if(i > 0 and maze[i-1][j] == '.'):
33                    nextQueue.append((i-1, j))
34                
35                if(i < len(maze) - 1 and maze[i+1][j] == '.'):
36                    nextQueue.append((i+1, j))
37                
38                if(j > 0 and maze[i][j-1] == '.'):
39                    nextQueue.append((i, j-1))
40                
41                if(j < len(maze[i]) - 1 and maze[i][j+1] == '.'):
42                    nextQueue.append((i, j+1))
43
44            currQueue = nextQueue
45            nextQueue = deque()
46            count += 1
47
48        return -1