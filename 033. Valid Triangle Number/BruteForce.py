def triangleNumber(nums):
    count = 0
    
    nums.sort()
    
    for i1 in range(len(nums)):
        for i2 in range(i1 + 1, len(nums)):
            for i3 in range(i2 + 1, len(nums)):
                
                condition1 = nums[i1] +  nums[i2] >  nums[i3]
                condition2 = nums[i1] +  nums[i3] >  nums[i2]
                condition3 = nums[i2] +  nums[i3] >  nums[i1]
                
                if condition1 and condition2 and condition3:  count += 1
                    
    return count

nums = [2,2,3,4]

print("Number of valid triplets -> ", triangleNumber(nums))