from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average=curr_average = sum(nums[:k])
        for i in range(k,len(nums)):
            curr_average = curr_average-nums[i-k] +nums[i]
            max_average = max(max_average,curr_average)
        return max_average/k

sol = Solution()
print(sol.findMaxAverage(nums=[1,12,-5,-6,50,3], k = 4))