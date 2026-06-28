class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict1 = {}
        result = []
        n = len(nums)
        for i in range(n):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]]+=1
        for key in dict1:
            if dict1[key] >n/3:
                result.append(key)
        return result
