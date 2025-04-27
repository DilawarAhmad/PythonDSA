from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_sum,max_sum,current_min,min_sum ,total_sum =  nums[0],nums[0],nums[0],nums[0],nums[0]
        for num in nums[1:]:
            current_sum = max(num,current_sum+num)
            max_sum = max(max_sum,current_sum)
            current_min = min(num,current_min+num)
            min_sum = min(current_min,min_sum)
            total_sum = total_sum+num
        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        else:
            return max_sum
sol =Solution()
print(sol.maxSubarraySumCircular(nums=[-3,-2,-3]))