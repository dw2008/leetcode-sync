class Solution:
    #input: string s, string t of equal length, maxCost
    #output: max length of a substring that can be changed to t within cost
    #strategy: using sliding window algorithm, first calculate the initial cost of length 1 that starts at left = 0 and store that cost. then, start right = 1 and increment right, shrinking left if cost is too 
    #edge cases: if there are no changes able to be made, return 0
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        cost = 0
        maxLen = 0
        
        for right in range(len(s)):
            cost += abs(ord(s[right])-ord(t[right]))

            while cost > maxCost:
                cost -= abs(ord(s[left])-ord(t[left]))
                left += 1

            maxLen = max(maxLen, right-left+1)
        
        return maxLen