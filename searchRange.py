class Solution:
    def searchRange(self, nums, target: int):
        return [self.first(nums,target),self.second(nums,target)]
    def first(self,nums,target):
        ans = -1
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                ans = mid
                high = mid-1
            elif nums[mid] < target:
                low = mid +1
            else:
                high = mid-1
        return ans
    def second(self,nums,target):
        ans = -1
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                ans = mid
                low = mid+1
            elif nums[mid] < target:
                low = mid +1
            else:
                high = mid-1
        return ans

sol = Solution()
# Target appears multiple times in the middle
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 8))   # [3,4]

# Target not present but in range of numbers
print(sol.searchRange(nums = [5,7,7,8,8,10], target = 6))   # [-1,-1]

# Empty array
print(sol.searchRange(nums = [], target = 0))               # [-1,-1]

# Single element, matches target
print(sol.searchRange(nums = [1], target = 1))              # [0,0]

# Single element, doesn’t match target
print(sol.searchRange(nums = [1], target = 0))              # [-1,-1]

# All elements same as target
print(sol.searchRange(nums = [2,2,2,2,2], target = 2))      # [0,4]

# Target smaller than all elements
print(sol.searchRange(nums = [3,4,5,6], target = 1))        # [-1,-1]

# Target greater than all elements
print(sol.searchRange(nums = [3,4,5,6], target = 7))        # [-1,-1]

# Target at very start
print(sol.searchRange(nums = [1,1,2,3,4], target = 1))      # [0,1]

# Target at very end
print(sol.searchRange(nums = [1,2,3,4,4], target = 4))      # [3,4]



        