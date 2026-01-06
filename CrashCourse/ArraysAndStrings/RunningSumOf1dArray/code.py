class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = [nums[0]]
        
        for i in range(1, len(nums)):
            answer.append(nums[i] + answer[-1])
        
        return answer
        
