from typing import List
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        new = []
        for num in nums:
            if num in new:
                return num
            new.append(num)
sol =Solution()
print(sol.repeatedNTimes(nums=[5,1,5,2,5,3,5,4]))