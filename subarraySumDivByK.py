from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum +=num
            mod = ((prefix_sum%k)+k)%k
            if mod in dic:
                count += dic[mod]
            if mod not in dic:
                dic[mod] = 0
            dic[mod] += 1

        return count
new = Solution()
print(new.subarraysDivByK(nums= [4,5,0,-2,-3,1], k = 5))