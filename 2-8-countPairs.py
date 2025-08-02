class Solution:
    def countPairs(self, arr, k):
        freq ={}
        count = 0
        for num in arr:
            if num + k in freq:
                count += freq[num+k]
            if num - k in freq:
                count += freq[num - k]
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        return count
sol = Solution()
print(sol.countPairs([1, 2, 3, 4, 5], 2))
print(sol.countPairs([1, 2, 3, 4, 5], 1))
print(sol.countPairs([1, 2, 3, 4, 5], 3))