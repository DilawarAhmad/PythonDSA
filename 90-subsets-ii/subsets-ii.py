class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subsets = []
        self.subsetsWithRec(nums,subsets,0,result)
        return result

    def subsetsWithRec(self,nums,subsets,i,result):
        if len(nums) == i:
            result.append(subsets[:])
            return
        subsets.append(nums[i])
        self.subsetsWithRec(nums,subsets,i+1,result)
        subsets.pop()
        j = i+1
        while (j<len(nums) and nums[j] == nums[j-1]):
            j+=1  
        self.subsetsWithRec(nums,subsets,j,result)
