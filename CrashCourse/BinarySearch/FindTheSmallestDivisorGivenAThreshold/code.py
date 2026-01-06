class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def check(mid):
            result = 0

            for num in nums:
                result += math.ceil(num / mid)
            
            return result <= threshold

        left = 1
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2
            
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
