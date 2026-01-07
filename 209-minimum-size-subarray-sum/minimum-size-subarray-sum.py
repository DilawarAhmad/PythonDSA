class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_ = 0
        min_sum = float('inf')
        for right in range(len(nums)):
            sum_ += nums[right]
            while sum_ >= target:
                min_sum = min(min_sum,right-left+1)
                sum_ -= nums[left]
                left+=1
        return 0 if min_sum == float('inf') else min_sum