class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums,0,result)
        return result
    def backtrack(self,nums,idx,result):
        if (idx == len(nums)):
            result.append(nums[:])
            return 
        for i in range(idx,len(nums)):
            nums[i] ,nums[idx] = nums[idx],nums[i]
            self.backtrack(nums,idx+1,result)
            nums[i],nums[idx] = nums[idx],nums[i]
