class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack =[]
        result =[0] *n
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if i<n:
                result[i%n] = stack[-1] if stack else -1
            stack.append(nums[i%n])

        return result