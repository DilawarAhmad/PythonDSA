from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(path,used):
            if (len(path)==len(nums)):
                result.append(path[:])
                return 
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path,used)
                    path.pop()
                    used[i] = False
        used = [False]*len(nums)
        backtrack([],used)
        return result
sol = Solution()
print(sol.permute([1,2,3]))