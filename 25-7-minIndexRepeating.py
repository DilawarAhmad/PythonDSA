class Solution:
    def firstRepeated(self,arr):
        maps = {}
        seen = set()
        for i,num in enumerate(arr):
            if num in maps:
                seen.add(num)
            else:
                maps[num] = i
        min_index = float('inf')
        for num in seen:
            min_index = min(min_index, maps[num])
        return min_index if min_index != float('inf') else -1
sol = Solution()
print(sol.firstRepeated([6, 3, 4, 5, 1, 2, 3, 4, 5]))  
print(sol.firstRepeated([1, 2, 3, 4, 5]))