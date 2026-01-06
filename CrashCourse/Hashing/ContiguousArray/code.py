class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLength = 0
        count = 0
        countMap = {}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            
            if count == 0:
                maxLength = i + 1
            
            if count in countMap:
                maxLength = max(maxLength, i - countMap[count])
            else:
                countMap[count] = i
                
        return maxLength
