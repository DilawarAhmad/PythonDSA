class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(map(int,str(n)))
        n = len(digits)
        i = n-2
        while i>=0 and digits[i] >= digits[i+1]:
            i-=1
        if i<0:
            return -1
        j = n-1
        while j>=0 and digits[j]<= digits[i]:
            j-=1
        digits[j],digits[i] = digits[i],digits[j]
        digits[i+1:] = reversed(digits[i+1:])
        result = int("".join(map(str,digits)))
        return result if result<=2**31 -1 else -1