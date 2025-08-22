class Solution:
    def evaluate(self, arr):
        stack =[]
    
        for i in arr:
            if i == "+" or i == "-" or i=="/" or i=="*":
                item1 = stack.pop()
                item2 = stack.pop()
                if i=="+":
                    result = item2+item1
                elif i == "-":
                    result = item2-item1
                elif i=="*":
                    result = item2*item1
                else:
                    result = int(item2/item1)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[0]
sol = Solution()
print(sol.evaluate(arr = ["2", "3", "1", "*", "+", "9", "-"]))
print(sol.evaluate(arr = ["100", "200", "+", "2", "/", "5", "*", "7", "+"]))
print(sol.evaluate(arr=["-8","3","/"]))
