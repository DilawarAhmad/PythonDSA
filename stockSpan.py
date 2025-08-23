class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        result = [0]*n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if not stack:
                result[i] = i+1
            else:
                result[i] = i-stack[-1]
            stack.append(i)
        return result
sol =Solution()
print(sol.calculateSpan(arr = [100, 80, 60, 70, 60, 75, 85]))
print(sol.calculateSpan(arr=[50, 50]))