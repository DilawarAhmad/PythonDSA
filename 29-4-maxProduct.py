from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product , current_max , current_min = nums[0],nums[0],nums[0]
        for num in nums[1:]:
            if num<0:
                current_max , current_min = current_min,current_max
            current_max = max(num,num*current_max)
            current_min = min(num , num* current_min)
            max_product = max(max_product,current_max)

        return max_product
sol = Solution()
print(sol.maxProduct(nums= [-2,3,-4]))