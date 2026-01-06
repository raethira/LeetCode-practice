class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = lastBroken = 0
        indexMap = {}
        
        for index, char in enumerate(s):
                
            if char in indexMap:
                if indexMap[char] >= lastBroken:
                    lastBroken = indexMap[char] + 1
                    
            answer = max(answer, index - lastBroken + 1)
                
            indexMap[char] = index
                
        return answer
