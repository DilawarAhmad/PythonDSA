from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        q = deque()
        result = []
        for i in range(n):
            if q and q[0] <= i-k:
                q.popleft()
            while q and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)
            if i>=k-1:
                result.append(arr[q[0]])
        return result


sol = Solution()
print(sol.maxOfSubarrays(arr = [1, 2, 3, 1, 4], k = 1))
print(sol.maxOfSubarrays(arr=[8, 5, 10, 7, 9, 4, 15, 12], k = 4))
print(sol.maxOfSubarrays(arr=[1],k=1))