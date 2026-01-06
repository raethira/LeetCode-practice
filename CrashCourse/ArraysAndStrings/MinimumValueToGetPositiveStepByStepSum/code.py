class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        
        for i in range (1, len(nums)):
            prefixSum.append(nums[i] + prefixSum[-1])
            
        minOfPrefixSum = min(prefixSum)
        
        if minOfPrefixSum < 0:
            return 1 + abs(minOfPrefixSum)
        
        return 1
        
