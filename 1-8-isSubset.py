from collections import Counter
class Solution:
    def isSubset(self, a, b):
        count_b = Counter(b)
        count_a = Counter(a)
        for elem in count_b:
            if count_b[elem] > count_a.get(elem,0):
                return False
        return True
sol = Solution()
print(sol.isSubset([1, 2, 3], [1, 2, 3, 4]))
print(sol.isSubset([1, 2, 3], [4, 5, 6]))