def specialArray(nums): 
    # x can be in the range 0 to length of the list (inclusive)
    # We need to go through the whole array for each value of x
    for x in range(len(nums) + 1):
        count = 0
        for num in nums:
            if num >= x: count += 1
        # If count of elements >= x is equal to x
        # That means, this is a special array so we can return x
        if count == x: return x
        
    # If not a special array
    return -1


nums = [0,4,3,0,4]

print("Output ->", specialArray(nums))