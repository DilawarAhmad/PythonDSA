from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        result =[]
        for i in range(len(sort)):
            if i > 0 and sort[i] == sort[i-1]: 
                continue
            left = i + 1
            right = len(sort) - 1
            while left < right:
                total = sort[i] + sort[left] + sort[right]
                if total == 0:
                    result.append([sort[i], sort[left], sort[right]])
                    while left < right and sort[left] == sort[left+1]:
                        left += 1
                    while left < right and sort[right] == sort[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
sol = Solution()
print(sol.threeSum(nums=[-1,0,1,2,-1,-4]))