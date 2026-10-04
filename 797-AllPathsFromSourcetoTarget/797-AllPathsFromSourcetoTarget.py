# Last updated: 10/4/2026, 6:57:53 PM
1class Solution:
2    """
3    using backtracking: want to get all paths to the end, so we want to use backtracking and find
4    all the possible paths and append them to a list. go recursively: base case: current node = end,
5    append current path to the result; otherwise, for each possible neighbor at this point, if not 
6    in the path, call the backtrack function with this node and the current path, and pop the node
7    out after the backtrack fuhnction for that node is done. return the resulting path list.
8    """
9    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
10        result = []
11        
12        def backtrack(node, path):
13            if(node == len(graph)-1):
14                result.append(list(path))
15                return
16            
17            
18            for neighbor in graph[node]:
19                if(neighbor not in path):
20                    path.append(neighbor)
21                    backtrack(neighbor, path)
22                    path.pop()
23            
24        backtrack(0, [0])
25        return result