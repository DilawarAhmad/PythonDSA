class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        if n<3:
            return 0
        increasing = [0]*n
        decreasing = [0]*n
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                increasing[i] = increasing[i-1]+1
        for i in range(n-2,-1,-1):
            if arr[i]>arr[i+1]:
                decreasing[i] = decreasing[i+1]+1
        for i in range(n):
            if increasing[i]>0 and decreasing[i]>0:
                result = max(result,increasing[i]+decreasing[i]+1)
        return result