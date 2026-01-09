class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        count = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j+=1
                nums[j] = nums[i]
                count = 0
            else:
                count+=1
                if count<=1:
                    j +=1
                    nums[j] = nums[i]
                else:
                    continue
        return j+1
                
