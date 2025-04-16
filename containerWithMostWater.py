def most(nums):
    left = 0
    right = len(nums)-1
    max_area = 0
    while left < right:
        area = min(nums[left],nums[right])*(right-left)
        max_area = max(area,max_area)
        if nums[left] < nums[right]:
            left +=1
        else:
            right-=1
        
    return max_area
print(most(nums=[1,8,6,2,5,4,8,3,7]))