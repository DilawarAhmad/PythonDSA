class Solution:
    def countAndSay(self, n: int) -> str:
        first_term = "1"
        for i in range(n-1):
            current = []
            count = 1
            for i in range(1,len(first_term)):
                if first_term[i] == first_term[i-1]:
                    count+=1
                else:
                    current.append(str(count))
                    current.append(first_term[i-1])
                    count=1
            current.append(str(count))
            current.append(first_term[-1])
            first_term = "".join(current)
        return first_term