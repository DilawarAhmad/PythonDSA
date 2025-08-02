class Solution:
    def minRemove(self, arr1, arr2):
        freq1 = {}
        freq2 = {}
        count =0
        for num in arr1:
            if num in freq1:
                freq1[num] +=1
            else:
                freq1[num] = 1
        for num in arr2:
            if num in freq2:
                freq2[num] +=1
            else:
                freq2[num] = 1
        for num in freq1:
            if num in freq2:
                count += min(freq1[num],freq2[num])
        return count
sol = Solution()
print(sol.minRemove([1, 2, 3, 4], [2, 3, 5, 6]))
print(sol.minRemove([1, 2, 2, 3], [2, 2, 3, 4]))
print(sol.minRemove([1, 2, 3], [4, 5, 6]))