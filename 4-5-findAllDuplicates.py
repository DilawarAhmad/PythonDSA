from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            index = abs(num) -1
            if nums[index]<0:
                result.append(abs(num))
            else:
                nums[index]*=-1
        return result
    
sol =Solution()
print(sol.findDuplicates(nums=[4,3,2,7,8,2,3,1]))