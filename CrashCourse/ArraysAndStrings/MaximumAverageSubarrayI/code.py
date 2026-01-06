class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:        
        
        answer = windowSum = sum(nums[0:k]) 
        
        for left in range(len(nums) - k):
            windowSum = windowSum - (nums[left])
            windowSum = windowSum + (nums[left + k])
            
            answer = max(answer, windowSum)
            
        return answer / k
