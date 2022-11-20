def waysToSplit(nums):  
    n = len(nums)
    mod = pow(10,9) + 7
        
    # First, we convert the given array into a prefix sum array
    for i in range(1, n): nums[i] = nums[i - 1] + nums[i]
            
            
    # Suppose the "left" subarray ends at index "left"
    # Suppose the "mid" subarray starts at index "left + 1" and ends at index "mid"
    # And finally, suppose the "right" subarray starts at index "mid + 1" and ends at index "right"
        
    # The prefix sum array will help in such a way that
        
    # To find the sum of "mid" subarray, all we need to do is nums[mid] - nums[left]
    # To find sum of "left" subarray, we just do nums[left]
    # To find sum of "right" subarray, we just do nums[right] - nums[mid]
        
    waysToSplit = 0
        
    # Here, each "i" is the last index of "left" subarray
    # So, for every possible "i" value, we try to see how many ways are there to split
    for i in range(n):
            
        # For each "i", we will see what can be the leftmost valid position of "mid" subarray's right boundary
        # That is, how much left we can keep the right boundary of "mid" subarray
        # Such that the condition is still true
            
        # Since the "mid" subarray starts where the "left" subarray ends
        # It means, start is "i + 1" since till "i" we have the "left" subarray
            
        start = i + 1
            
        # Since the "mid" subarray ends where the "right" subarray starts
        # the maximum we can keep the right boundary of "mid" is at "N-2"
        end = n - 2
            
        leftmostIndex = -1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            leftSubarraySum = nums[i]
            midSubarraySum = nums[mid] - nums[i]
            rightSubarraySum = nums[n - 1] - nums[mid]
                
            # if at "mid" the left subarray sum is <= mid subarray sum
            # And the mid subarray sum is <= right subarray sum
            # Then this is one possible way to split
            # But we are looking for the leftmost valid position of "mid" subarray's boundary
            # So keep searching on left side   
            if (leftSubarraySum <= midSubarraySum) and (midSubarraySum <= rightSubarraySum):
                leftmostIndex = mid
                end = mid - 1
            # If the leftsubarray sum is greater than mid subarray sum
            # We need to increase the size of mid subarray so that its sum is bigger
            # That is, its boundary should be placed at an index more than "mid"
            # That's why we do start = mid + 1
            elif leftSubarraySum > midSubarraySum:
                start = mid + 1      
            # Otherwise, we can shift the boundary to left of mid as the leftsubarray sum is <= midsubarray sum
            else: end = mid - 1
            
        # If leftmostIndex is -1, no need to continue further. We can skip this iteration
        if leftmostIndex == -1: continue
            
        # *********************************************************************************
                                                      
        # Now, for each "left" boundary index "i", we will see what can be the rightmost valid position of "mid" index
        # That is, how much right we can keep the right boundary of "mid" subarray
        # Such that the condition is still true
            
        start = i + 1
        end = n - 2
            
        rightmostIndex = -1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            leftSubarraySum = nums[i]
            midSubarraySum = nums[mid] - nums[i]
            rightSubarraySum = nums[n - 1] - nums[mid]
                
            # if at "mid" the left subarray sum is <= mid subarray sum
            # And the mid subarray sum is <= right subarray sum
            # Then this is one possible way to split
            # But we are looking for the rightmost valid position of "mid" subarray's boundary
            # So keep searching on right side   
            if (leftSubarraySum <= midSubarraySum) and (midSubarraySum <= rightSubarraySum):
                rightmostIndex = mid
                start = mid + 1
            # If the leftsubarray sum is greater than mid subarray sum
            # We need to increase the size of mid subarray so that its sum is bigger
            # That is, its boundary should be placed at an index more than "mid"
            # That's why we do start = mid + 1
            elif leftSubarraySum > midSubarraySum:
                start = mid + 1      
            # Otherwise, we can shift the boundary to left of mid as the leftsubarray sum is <= midsubarray sum
            else: end = mid - 1
            
            
        if rightmostIndex != -1: 
            waysToSplit += (rightmostIndex - leftmostIndex + 1)

    return waysToSplit % mod

nums = [1,2,2,2,5,0]

print("Ways to Split -> ",waysToSplit(nums))