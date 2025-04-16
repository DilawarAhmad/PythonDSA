from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i , j]
        return []
    
new = Solution()
print(new.twoSum(nums=[1,3,4,6,3,7],target=9))