class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        sum_set = 0
        set1 = set()
        for num in nums:
            if num not in set1:
                set1.add(num)
                sum_set+=num
            else:
                result.append(num)
        n = len(nums)
        sum_act = (n*(n+1))//2
        missing = sum_act - sum_set
        result.append(missing)
        return result
        