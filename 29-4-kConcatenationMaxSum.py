from typing import List
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        new_arr= arr+arr
        MOD = 10**9 + 7
        current_sum , kadan1 ,total_sum = arr[0],arr[0],arr[0]
        for num in arr[1:]:
            total_sum +=num
            current_sum = max(num,current_sum+num)
            kadan1 = max(current_sum,kadan1)
        current_sum , kadan2 = new_arr[0],new_arr[0]
        for num in new_arr[1:]:
            current_sum = max(num,current_sum+num)
            kadan2= max(current_sum,kadan2)
        if k==1:
            return max(0,kadan1) % MOD
        if k==2:
            return max(0,kadan2)%MOD
        if k>=3:
            if total_sum > 0:
                result = kadan2 + (k - 2) * total_sum
            else:
                result = kadan2
            return max(0, result) % MOD
            
sol = Solution()
print(sol.kConcatenationMaxSum(arr =[10000,10000,10000,10000,10000,10000,10000,10000,10000,10000], k =100000))