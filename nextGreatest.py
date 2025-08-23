
class Solution:
    def nextGreaterElement(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(2 * n):
            cur = nums[i % n]
            while stack and nums[stack[-1]] < cur:
                idx = stack.pop()
                result[idx] = cur
            if i < n:
                stack.append(i)

        return result

sol = Solution()
print(sol.nextGreaterElement(nums = [1,2,1]))
print(sol.nextGreaterElement(nums=[1,2,3,4,3]))
print(sol.nextGreaterElement(nums = [5]))
print(sol.nextGreaterElement(nums = [1,2,3,4,5]))
print(sol.nextGreaterElement(nums =[5,4,3,2,1]))
print(sol.nextGreaterElement(nums=[7,7,7,7]))


