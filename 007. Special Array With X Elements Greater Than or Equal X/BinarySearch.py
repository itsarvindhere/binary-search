def specialArray(nums):
        
    # Sort the given array
    nums.sort()
        
    n = len(nums)
        
    # Now, for each value of x, we just need to find the smallest number that is >= x
    # Once we find that, all numbers after that number are already >= x as array is sorted
        
    for x in range(n + 1):
            
        # Binary Search
        start = 0
        end = n - 1
        result = -1
            
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] >= x:
                result = mid
                end = mid - 1
            else:
                start = mid + 1
                    
        if result >= 0 and n - result == x: return x
            

    # If not a special array
    return -1


nums = [0,4,3,0,4]

print("Output ->", specialArray(nums))