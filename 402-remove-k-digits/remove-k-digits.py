class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        digits = list(map(int,num))
        n = len(digits)
        for i in range(n):
            while stack and k>0 and stack[-1] > digits[i]:
                stack.pop()
                k-=1
            stack.append(digits[i])
        if k>0:
            stack = stack[:-k]
        result ="".join(map(str,stack)).lstrip('0')
        return result if result else '0'
