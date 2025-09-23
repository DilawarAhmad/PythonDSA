class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low = 0
        high = len(nums)-1
        return self.binary(nums,low,high,target)
    def binary(self,nums,low,high,target):
        if low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.binary(nums,mid+1 , high , target)
            elif nums[mid] > target:
                return self.binary(nums,low , mid-1 , target)
        else:
            return low

sol = Solution()
print(sol.searchInsert(nums = [1,3,5,6], target = 5))
print(sol.searchInsert(nums = [1,3,5,6], target = 2))
print(sol.searchInsert(nums = [1,3,5,6], target = 7))