from collections import Counter

class Solution:
    """
    use a combination of hashmap and sliding window. starting from the left, increase to the right when
    no duplicates in the window, shrink left when there are duplicates in window. check the number of 
    each character by using hashmap and incrementing/decrementing value when added/removed from window.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = Counter()
        left = 0
        right = 0
        res = 0
        
        while right < len(s):
            window[s[right]] += 1
            
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        
        return res
                