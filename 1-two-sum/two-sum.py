class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i , num in enumerate(nums):
            needed = target-num
            if needed in dict1:
                return [dict1[needed],i]
            dict1[num] = i