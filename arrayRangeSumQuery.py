from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = nums[:]
        for i in range(1,len(nums)):
            self.prefix_sum[i] += self.prefix_sum[i-1]
    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.prefix_sum[right]
        else:
            return self.prefix_sum[right] - self.prefix_sum[left-1]


# Your NumArray object will be instantiated and called as such:
obj = NumArray(nums=[-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(left=0,right=2)
print(param_1)
param_2 = obj.sumRange(left=2,right=5)
print(param_2)
param_3 = obj.sumRange(left=0,right=5)
print(param_3)