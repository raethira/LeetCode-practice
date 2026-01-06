class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        
        while (left <= right):
            leftSq = nums[left] * nums[left]
            rightSq = nums[right] * nums[right]
            
            if leftSq < rightSq:
                result [right - left] = rightSq
                right -= 1
            else:
                result [right - left] = leftSq
                left += 1
            
        return result
