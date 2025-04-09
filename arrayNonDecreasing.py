def checkPossibility(nums) -> bool:
    n = len(nums)
    modified = False 
    for i in range(n - 1):
        if nums[i] <= nums[i+1]:
            continue 
        if modified:
            return False
        if i == 0 or nums[i-1] <= nums[i+1]:
            pass
        else:
            nums[i+1] = nums[i] 
        modified = True 
    return True


print(f"[5, 7, 1, 8] -> {checkPossibility([5, 7, 1, 8])}") # Expected: True
print(f"[1, 2, 5, 3, 4] -> {checkPossibility([1, 2, 5, 3, 4])}") # Expected: True
