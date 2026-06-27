class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            if i==0:
                result.append([1])
            elif i==1:
                result.append([1,1])
            else:
                list_ = []
                j_length = len(result[i-1])
                for j in range(j_length):
                    if j==0:
                        list_.append(1)
                    else:
                        element = result[i-1][j] + result[i-1][j-1]
                        list_.append(element)
                list_.append(1)
                result.append(list_)
        return result
