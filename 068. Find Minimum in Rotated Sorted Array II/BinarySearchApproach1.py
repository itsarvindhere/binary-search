def findMin(nums):
    # To remove the duplicates but keep the order
    nums = list(dict.fromkeys(nums))

    # Length
    n = len(nums)
        
    # Initialize minimum
    minimum = nums[0]
        
    start, end = 0, n - 1
        
    while start <= end:
            
        # Get the mid index
        mid = start + (end - start) // 2
            
        # Which sorted part "mid" belongs to?
            
        # If it belongs to the left sorted part
        if nums[start] <= nums[mid]:
                
            # Since it belongs to left sorted part,
            # The minimum element in this sorted part is the "start" element
            # Update minimum if required
            minimum = min(minimum, nums[start])
                
            # Now, we no longer need to care about this left sorted part
            start = mid + 1
                
        # If it belongs to the right sorted part
        else:
                
            # Since it belongs to right sorted part,
            # The minimum element in this sorted part is the "mid" element
            # Update minimum if required
            minimum = min(minimum, nums[mid])
                
            # Now, we no longer need to care about this right sorted part
            end = mid - 1
                
        
    # Return the minimum element
    return minimum

nums = [3,3,0,1]

print("Minimum is -> ", findMin(nums))