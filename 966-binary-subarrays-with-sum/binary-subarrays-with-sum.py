class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dict1 = {0:1}
        prefix = 0
        count = 0
        for i in range(len(nums)):
            prefix+=nums[i]
            left = prefix-goal
            if left in dict1:
                count+=dict1[left]
            if prefix not in dict1:
                dict1[prefix] = 0
            dict1[prefix]+=1
        return count