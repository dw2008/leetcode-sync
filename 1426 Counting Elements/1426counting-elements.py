class Solution:
    def countElements(self, arr: List[int]) -> int:
        dic = set(arr)
        count = 0
        
        for i in arr:
            if i+1 in dic:
                count += 1
        
        return count