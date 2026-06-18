class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        prev_max = 0
        for i in nums:
            if i==0:
                if prev_max < max_count:
                    prev_max = max_count
                max_count= 0
            else:
                max_count+=1
        return prev_max if prev_max>max_count else max_count
