class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(a)
        m = len(b)
        k = ceil(m/n)
        s = a*k
        if b in s:
            return k
        s = a*(k+1)
        if b in s:
            return k+1
        return -1