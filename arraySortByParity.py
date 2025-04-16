def parity(nums):
    n = len(nums)
    left =[]
    right = []
    for i in range(n):
        if nums[i]%2 ==0:
            left.append(nums[i])
        else:
            right.append(nums[i])
    return left+right
print(parity(nums=[1,3,2,4,5,6,8,9]))