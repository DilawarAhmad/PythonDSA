class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-1-i]:
                return False
        return True
sol = Solution()
print(sol.isPalindrome("racecar"))
print(sol.isPalindrome("hello"))