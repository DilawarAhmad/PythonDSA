from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_num= set(nums)
        max_length = 0
        for num in set_num:
            if num-1 not in set_num:
                current_num=  num
                current_length = 1
                while current_num +1 in set_num:
                    current_num +=1
                    current_length+=1
                max_length = max(current_length,max_length)
        return max_length
sol = Solution()
print(sol.longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1]))
