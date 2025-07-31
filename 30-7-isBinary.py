class Solution:
    def isBinary(self, s):
        for i in range(len(s)):
            if s[i]!='0' and s[i]!='1':
                return False
        return True
        
sol = Solution()
print(sol.isBinary("101010"))
print(sol.isBinary("12345"))