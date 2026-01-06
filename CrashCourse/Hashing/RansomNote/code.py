class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = Counter(magazine)
        
        for s in ransomNote:
            if s in magazineMap:
                magazineMap[s] -= 1
                if magazineMap[s] == 0:
                    del magazineMap[s]
            else:
                return False
            
        return True
