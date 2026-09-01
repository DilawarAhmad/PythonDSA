class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for start in range(n-m+1):
            match = True
            for i in range(m):
                if haystack[start+i]!=needle[i]:
                    match = False
                    break
            if match:
                return start
        return -1