from typing import List
class Solution:
    def minOperations(self, n: int) -> int:
        left = 0
        right = n-1
        result = 0
        while left < right:
            result+=n- (2*left+1)
            left += 1
            right -= 1
        return result
sol= Solution()
print(sol.minOperations(n=6))