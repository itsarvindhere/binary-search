# Helper method for Binary Search
def binarySearch(i, start, end, nums, isLeftSearch):
    n = len(nums)
        
    index = -1
    while start <= end:
        mid = start + (end - start) // 2
                
        leftSubarraySum = nums[i]
        midSubarraySum = nums[mid] - nums[i]
        rightSubarraySum = nums[n - 1] - nums[mid]
                

        if (leftSubarraySum <= midSubarraySum) and (midSubarraySum <= rightSubarraySum):
                index = mid
                if isLeftSearch: end = mid - 1
                else: start = mid + 1
        elif leftSubarraySum > midSubarraySum:
            start = mid + 1      
        else: end = mid - 1
                
    return index
 
def waysToSplit(nums):
        
    # Why did the above solution gave TLE?
    # Because for each "i", we have to go through each possible "j"
    # Instead of this, what if we can find the leftmost valid "j" and rightmost valid "j"
    # In that way, the number of ways for that "i" is simply "rightmostIndex - leftmostIndex + 1"
    # ANd that's where the Binary Search approach comes into picture.
        
    n = len(nums)
        
    # First, we convert the given array into a prefix sum array
    for i in range(1, n): nums[i] = nums[i - 1] + nums[i]
        
    ways = 0
        
    # Here, each "i" is the last index of "left" subarray
    # So, for every possible "i" value, we try to see how many ways are there to split
    # Since "mid" and "right" subarrays need to have at least one element
	# The last index of "left" subarray can be up to "n-3" index
    for i in range(n-2):
            
        # For each "i", we will see what can be the leftmost valid position of "mid" subarray's right boundary
        # That is, how much left we can keep the right boundary of "mid" subarray
        # Such that the condition is still true
            
        leftmostIndex = binarySearch(i, i + 1, n - 2, nums, True)

        # If leftmostIndex is -1, no need to continue further. We can skip this iteration
        if leftmostIndex == -1: continue
                                    
        # Now, for each "left" boundary index "i", we will see what can be the rightmost valid position of "mid" index
        # That is, how much right we can keep the right boundary of "mid" subarray
        # Such that the condition is still true
            
        rightmostIndex = binarySearch(i, i + 1, n - 2, nums, False)
            
        if rightmostIndex != -1: ways += (rightmostIndex - leftmostIndex + 1)

    return ways % 1000000007

nums = [1,2,2,2,5,0]

print("Ways to Split -> ", waysToSplit(nums))