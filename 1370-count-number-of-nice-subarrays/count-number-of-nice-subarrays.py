class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        odd_c = 0
        prefix = 0
        result = 0
        for right in range(len(nums)):
            if nums[right]%2:
                odd_c +=1
                prefix = 0
            while odd_c == k:
                prefix+=1
                if nums[left]%2:
                    odd_c -=1
                left+=1
            result+=prefix
        return result
