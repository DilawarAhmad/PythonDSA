class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        if n<=0:
            return []
        elif n ==1:
            return [0]
        elif n==2:
            return [0,1]
        else:
            lis = self.fibonacciNumbers(n-1)
            new = lis[-1] + lis[-2]
            lis.append(new)
            return lis
sol = Solution()
print(sol.fibonacciNumbers(10))
print(sol.fibonacciNumbers(0))