# Helper method to check if we can split array into "k" subarrays
# Such that the largest sum does not exceed "maxSum"
def isValid(maxSum, nums, k):
    subarrays = 0
        
    subArraySum = 0
    for num in nums:
        subArraySum += num
            
        if subArraySum > maxSum:
            subarrays += 1
            subArraySum = num
                
    # Last Subarray
    subarrays += 1
        
    return subarrays <= k

    
def splitArray(nums, k):
    # Binary Search on Answer
    # We have to Minimize the "Largest Sum"
        
    # So, what can be the lower and upper bound of the sum?
    # The smallest value of the largest sum can be the maximum in the list
    start = max(nums)
        
    # And the max value of largest possible sum can be the sum of whole array
    end = sum(nums)
        
    # And so, in this range, we have to minimize the "Largest" sum
    # It means, each value in this range is the "Largest Sum" that a subarray has
        
    minimizedSum = -1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If we can split this list into "k" subarrays 
        # such that the largest sum among those subarrays is "mid"
        # Then "mid" is one possible solution
        # But since we are asked to minimize this value
        # We save this "mid" value and keep searching on left side of mid
        if isValid(mid, nums, k):
            minimizedSum = mid
            end = mid - 1
            
        # Otherwise, if "mid" itself cannot be valid, no value smaller than "mid" is valid
        # So, in that case, search on right side of "mid"
        else: start = mid + 1
        
        
    return minimizedSum

nums = [7,2,5,10,8]
k = 2

print("Minimized Largest Sum is -> ", splitArray(nums, k))