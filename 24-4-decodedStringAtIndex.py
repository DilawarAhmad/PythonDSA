from typing import List
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_len = 0
        for char in s:
            if char.isdigit():
                total_len = total_len * int(char)
            else:
                total_len +=1
        for char in s[::-1]:
            if char.isdigit():
                total_len = total_len//int(char)
                k = k% int(total_len)
                if k==0:
                    k= total_len
            elif not char.isdigit() and total_len==k:
                return char
            else:
                total_len -=1
sol = Solution()
print(sol.decodeAtIndex(s='leet2code3',k=10))