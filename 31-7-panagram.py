class Solution:
    def checkPangram(self,s):
        s = s.lower()
        for char in "abcdefghijklmniopqrstuvwxyz":
            if char not in s:
                return False
        return True
sol = Solution()
print(sol.checkPangram("The quick brown fox jumps over the lazy dog"))
print(sol.checkPangram("Hello World"))