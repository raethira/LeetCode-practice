class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = answer = counter = 0
        n = len(nums)
        
        for left in range(n):
            while right < n and (counter < k or nums[right] == 1):
                if(nums[right] == 0):
                    counter += 1
                right += 1
            
            answer = max(answer, right - left)
            
            if(nums[left] == 0):
                counter -= 1
        
        return answer
