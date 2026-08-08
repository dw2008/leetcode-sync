# Last updated: 8/8/2026, 9:17:55 AM
1from collections import deque
2
3class MovingAverage:
4
5    def __init__(self, size: int):
6        self.size = size
7        self.queue = deque()
8        self.runningSum = 0
9
10    def next(self, val: int) -> float:
11        if len(self.queue) < self.size:
12            self.queue.append(val)
13        else:
14            self.runningSum -= self.queue.popleft()
15            self.queue.append(val)
16            
17        self.runningSum += val
18        return self.runningSum / len(self.queue)
19
20
21# Your MovingAverage object will be instantiated and called as such:
22# obj = MovingAverage(size)
23# param_1 = obj.next(val)