from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result =[]
        for num in nums2:
            if num in nums1 and num not in result:
                result.append(num)
        return result
    
sol = Solution()
print(sol.intersection(nums1=[1,2,2,1],nums2=[2,2]))