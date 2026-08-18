class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left = 0
        sum_ = nums[left]
        max_sum = sum_
        seen_set = {nums[left]}
        for right in range(1,len(nums)):
            while nums[right] in seen_set:
                sum_-=nums[left]
                seen_set.remove(nums[left])
                left+=1
            seen_set.add(nums[right])
            sum_ += nums[right]
            max_sum = max(max_sum, sum_)
        return max_sum
