class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0
        for chr in s:
            if chr=="(":
                if depth >0:
                    result.append(chr)
                depth +=1
            else:
                depth -=1
                if depth>0:
                    result.append(chr)
        return "".join(result)