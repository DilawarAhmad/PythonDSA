class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack1 = []

        for token in tokens:
            if token=="+":
                element1 , element2 = stack1.pop(), stack1.pop()
                stack1.append(element1+element2)
            elif token=="-":
                element1 , element2 = stack1.pop(), stack1.pop()
                stack1.append(element2-element1)
            elif token=="*":
                element1 , element2 = stack1.pop(), stack1.pop()
                stack1.append(element1*element2)
            elif token=="/":
                element1 , element2 = stack1.pop(), stack1.pop()
                stack1.append(int(element2/element1))
            else:
                stack1.append(int(token))
        return stack1[-1]