class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        stonesMap = Counter(stones)
        
        for s in jewels:
            if s in stonesMap:
                count += stonesMap[s] 
    
        return count
