class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        prefixSum = [nums[0]]
        
        for i in range(1, n):
            prefixSum.append(nums[i] + prefixSum[-1])
            
        print(prefixSum)
        answer = []
        
        for i in range(n):
            if (i - k) < 0 or (i + k) >= n:
                answer.append(-1)
            else:
                answer.append((prefixSum[i + k] - prefixSum[i - k] + nums[i - k]) // ((2 * k) + 1))
                
        return answer
            
