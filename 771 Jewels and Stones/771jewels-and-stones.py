class Solution:
    """
    use hashmap to store jewel values (faster than using an array) and then seeing if stones
    are in that jewel hashmap and then incrementing a jewel counter
    """
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jhash = dict()
        count = 0
        
        for jewel in jewels:
            jhash[jewel] = 0
        
        for stone in stones:
            if stone in jhash:
                count += 1
        
        return count