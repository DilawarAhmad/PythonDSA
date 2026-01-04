class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_pro =1
        left = [left_pro]
        for i in range(1,len(nums)):
            left_pro = left_pro *nums[i-1]
            left.append(left_pro)
        right_pro=1
        for i in range(len(nums)-2,-1,-1):
            right_pro = right_pro*nums[i+1]
            left[i] = left[i]*right_pro
        return left

            