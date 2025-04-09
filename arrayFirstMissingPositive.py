from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

# Example Usage:
solver = Solution()
print(f"[1, 2, 0] -> {solver.firstMissingPositive([1, 2, 0])}")          # Output: 3
print(f"[3, 4, -1, 1] -> {solver.firstMissingPositive([3, 4, -1, 1])}")    # Output: 2
print(f"[7, 8, 9, 11, 12] -> {solver.firstMissingPositive([7, 8, 9, 11, 12])}") # Output: 1
print(f"[] -> {solver.firstMissingPositive([])}")                      # Output: 1
print(f"[1] -> {solver.firstMissingPositive([1])}")                      # Output: 2
print(f"[2] -> {solver.firstMissingPositive([2])}")                      # Output: 1
