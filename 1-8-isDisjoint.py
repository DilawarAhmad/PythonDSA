class Solution:
    # Function to check if two arrays are disjoint
    def areDisjoint(self, a, b):
        set1 = set(a)
        set2 = set(b)
        set3 = set1.intersection(set2)
        return len(set3) == 0
        
sol = Solution()
print(sol.areDisjoint([1, 2, 3], [4, 5, 6]))
print(sol.areDisjoint([1, 2, 3], [2, 4, 5]))