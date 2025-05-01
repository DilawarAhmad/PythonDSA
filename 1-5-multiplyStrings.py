class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result1=0
        result2=0
        for char in num1:
            digit = ord(char)-ord('0')
            result1 = result1*10 +digit
        for char in num2:
            digit = ord(char)-ord('0')
            result2 = result2*10 +digit
        return str(result1*result2)
sol = Solution()
print(sol.multiply(num1 = "2", num2 = "3"))