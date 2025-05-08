from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left =0
        right = len(numbers)-1
        sum = 0
        while left<right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1,right+1]
            elif sum<target:
                left+=1
            else:
                right-=1
sol = Solution()
print(sol.twoSum(numbers = [2,3,4], target = 6))