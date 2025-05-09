class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n= len(nums)
        k = k%n
        if k == 0 or n <= 1:
            return
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)

    def reverse(self,nums,start,end):
        while start <end:
            nums[start],nums[end] =nums[end] ,nums[start]
            start +=1
            end -=1
    
