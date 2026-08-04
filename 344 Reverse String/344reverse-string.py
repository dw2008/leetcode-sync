class Solution:
    """
    using a pointer (i) from 0 to len(s)//2, swap s[i] and s[len(s)-i-1]
    """
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            x = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s)-i-1] = x
            
        