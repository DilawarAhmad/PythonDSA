from typing import List
from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] =1
        count = 0
        sum = 0
        for num in nums:
            sum += num%2
            count += dic[sum-k]
            dic[sum]+=1
        return count
sol = Solution()
print(sol.numberOfSubarrays(nums=[1,1,2,1,1], k = 3))
