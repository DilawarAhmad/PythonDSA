class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        return self.mergeSort(nums,low,high)

    def mergeSort(self,nums,low,high):
        if low>=high:
            return 0
        count = 0
        mid = (low+high)//2
        count+=self.mergeSort(nums,low,mid)
        count+=self.mergeSort(nums,mid+1,high)
        count+=self.countPairs(nums,low,mid,high)
        self.merge(nums,low,mid,high)
        return count
    def countPairs(self,nums,low,mid,high):
        count = 0
        right = mid+1
        for i in range(low,mid+1):
            while right<=high and nums[i]>2*nums[right]:
                right+=1
            count+= right-(mid+1)
        return count
    def merge(self,nums,low,mid,high):
        result_arr = []
        left = low
        right = mid+1
        while left<=mid and right<=high:
            if nums[left] <= nums[right]:
                result_arr.append(nums[left])
                left+=1
            else:
                result_arr.append(nums[right])
                right+=1
        while left<=mid:
            result_arr.append(nums[left])
            left+=1
        while right<=high:
            result_arr.append(nums[right])
            right+=1
        for i in range(low,high+1):
            nums[i] = result_arr[i-low]