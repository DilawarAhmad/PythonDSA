
class Solution:
    def longest(self,arr):
        maxi  =arr[0]
        count = 1
        for i in range(1,len(arr)):
            if arr[i] >= maxi:
                count +=1
                maxi = arr[i]
        return count
sol =Solution()
print(sol.longest(arr = [6, 2, 8, 4, 11, 13]))
print(sol.longest(arr=[2, 5, 3,7]))
print(sol.longest(arr=[1, 2, 3, 4, 5]))
print(sol.longest(arr=[5, 4, 3, 2, 1]))
print(sol.longest(arr=[7, 7, 7, 7]))
print(sol.longest(arr=[42]))
print(sol.longest(arr=[1, 10]))

