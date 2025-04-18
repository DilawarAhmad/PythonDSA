# Selection Sort
def sortArray( nums):
        for i in range(len(nums)):
            min_index = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min_index]:
                    min_index=j
            nums[min_index],nums[i] = nums[i],nums[min_index]
        return nums
print(sortArray(nums=[5,1,1,2,0,0]))

# #MergeSort
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left,right)

    def merge(self,left,right):
        result = []
        i,j = 0,0
        while i<len(left) and j <len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i = i+1
            else:
                result.append(right[j])
                j=j+1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

sol = Solution()
print(sol.sortArray([5, 2, 3, 1]))        # Output: [1, 2, 3, 5]
print(sol.sortArray([5, 1, 1, 2, 0, 0]))  # Output: [0, 0, 1, 1, 2, 5]
print(sol.sortArray([]))                 # Output: []
print(sol.sortArray([1]))                # Output: [1]
print(sol.sortArray([2, -1, 3]))          # Output: [-1, 2, 3]