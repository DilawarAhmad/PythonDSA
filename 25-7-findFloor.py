class Solution:
    def findFloor(self, arr, x):
        low = 0
        high = len(arr) - 1
        floor = -1
        while low<=high:
            mid = (low + high) //2
            if arr[mid] <= x:
                floor =mid
                low = mid +1
            else:
                high = mid - 1
        return floor
sol = Solution()
print(sol.findFloor([1, 2, 8, 10, 10, 12], 5))  
print(sol.findFloor([1, 2, 8, 10, 10,  12], 10))