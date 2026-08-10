# Last updated: 8/10/2026, 4:50:41 PM
1"""
2using a monotonically decreasing stack; store elements in a stack with format 
3[price, answer]. every time next is called, peek at stack[-1][0] and see if it is 
4leq the input. if it is, pop the element from the stack and push [price, stack[-1]
5[0]] onto the stack and return stack[-1][0] + 1. otherwise, return 1 by default. 
6(for first price, push answer = 0). a price to the left of a larger price will never
7be accessed so its okay to not re push everything.
8"""
9class StockSpanner:
10    def __init__(self):
11        self.stack = list()
12
13    def next(self, price: int) -> int:
14        count = 1
15        if not self.stack:
16            self.stack.append([price, 1])
17            return 1
18        
19        while self.stack and self.stack[-1][0] <= price:
20            count += self.stack.pop()[1]
21        self.stack.append([price, count])
22        return count
23
24
25# Your StockSpanner object will be instantiated and called as such:
26# obj = StockSpanner()
27# param_1 = obj.next(price)