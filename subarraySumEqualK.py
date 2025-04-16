from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum +=num
            if (prefix_sum -k) in dic:
                count += dic[prefix_sum-k]
            if prefix_sum not in dic:
                dic[prefix_sum] = 0
            dic[prefix_sum] += 1

        return count
new = Solution()
print(new.subarraySum(nums=[1,1,1],k=2))