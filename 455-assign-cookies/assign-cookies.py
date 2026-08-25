class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        left = right = 0
        while left<n and right<m:
            if g[left] <= s[right]:
                left+=1
                right+=1
            else:
                right+=1
        return left