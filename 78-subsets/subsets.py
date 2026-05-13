class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        sub = []
        self.allSubsets(nums,sub,0,result)
        return result
        
    def allSubsets(self,nums,sub,i,result):
        if i== len(nums):
            result.append(sub[:])
            return
        sub.append(nums[i])
        self.allSubsets(nums,sub,i+1,result)
        sub.pop()
        self.allSubsets(nums,sub,i+1,result)
