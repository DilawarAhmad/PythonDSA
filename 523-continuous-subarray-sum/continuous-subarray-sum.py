class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0: -1}
        runningSum = 0

        for i in range(len(nums)):
            runningSum += nums[i]

            if k != 0:
                remainder = runningSum % k
            else:
                remainder = runningSum

            if remainder in dic:
                if i - dic[remainder] >= 2:
                    return True
            else:
                dic[remainder] = i

        return False