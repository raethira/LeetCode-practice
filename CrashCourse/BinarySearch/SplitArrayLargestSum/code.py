class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(x):
            curr_sum = 0 
            splits = 0

            for num in nums:
           
                if (curr_sum + num) <= x:
                    curr_sum += num
                else:
                    curr_sum = num    # Start a new subarray with current number
                    splits += 1

            return (splits + 1) <= k    # (splits + 1) is the number of sub-arrays

        left = max(nums)  
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
