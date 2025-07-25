class Solution:
    def countZeroes(self, arr):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == 0:
                if mid == 0 or arr[mid - 1] != 0:
                    return len(arr) - mid
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return 0
sol = Solution()
print(sol.countZeroes([1, 0, 0, 0, 0, 0, 0])) 
print(sol.countZeroes([1, 1, 1, 1, 1, 1])) 