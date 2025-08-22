class Solution:
    def nextLargerElement(self,arr):
        n = len(arr)
        result = [-1]*n
        stack =[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(arr[i])
        return result
sol = Solution()
print(sol.nextLargerElement( arr= [1,5, 3, 2, 4]))
print(sol.nextLargerElement(arr=[5,4,6]))

