class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n= len(code)
        result = [0]*n
        if k==0:
            return result
        elif k>0:
            right_sum = sum(code[1:1+k])
            for i in range(n):
                result[i] =right_sum
                ele_out = (i+1)%n
                ele_in = (i+1+k)%n
                right_sum = right_sum - code[ele_out] + code[ele_in]
        elif k<0:
            k = -k
            left_sum = sum(code[n-k:])
            for i in range(n):
                result[i] = left_sum
                ele_out = (i-k)%n
                ele_in = i%n
                left_sum = left_sum -code[ele_out] + code[ele_in]
        return result