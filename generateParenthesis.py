class Solution:
    def generateParenthesis(self, n: int):
        result = []
        def backtrack(open, close,path):
            if open == n and close == n:
                result.append(path)
                return
            if open < n:
                backtrack(open+1, close , path+"(")
            if close < open:
                backtrack(open, close+1 , path+")")
        backtrack(0,0,"")
        return result
sol = Solution()
print(sol.generateParenthesis(n=3))
print(sol.generateParenthesis(n=4))