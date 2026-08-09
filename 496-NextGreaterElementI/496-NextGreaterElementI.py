# Last updated: 8/9/2026, 10:12:50 AM
1class Solution:
2    """
3    using a monotonically decreasing stack and a map; for every element of nums2, we first compare to the top
4    of the stack and see if it's greater than the top. if the element is greater than the top, we pop elements
5    from the stack until the stack is empty or the top of the stack is greater than the element. for each 
6    popped element, put the popped element+ element from nums2 in a hashmap. if the element from nums2 is less 
7    than or equal to the top, just push the element onto the stack. at the end, any remaining elements in the 
8    stack are mapped to -1. then, iterate through nums1 and find each value and put it in an answer array and 
9    return.
10    """
11    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
12        stack = list()
13        pairs = dict()
14        answer = list()
15
16        for n in nums2:
17            if not stack or n < stack[-1]:
18                stack.append(n)
19            else:
20                while stack and n > stack[-1]:
21                    top = stack.pop()
22                    pairs[top] = n
23                stack.append(n)
24
25        while stack:
26            pairs[stack.pop()] = -1
27
28        for n in nums1:
29            answer.append(pairs[n])
30        return answer