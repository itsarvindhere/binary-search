def waysToSplit(nums):    
    ways = 0        
    # Since there are three subarrays
    # It means, basically, there are two boundaries. 
    # left | mid | right => Here, each pipe (|) is a boundary
        
    # Wherever "left" subarray ends, let's say that index is "i"
    # Now for every "i", we can try to find the index where "mid" subarray ends
    # Such that, the condition given in problem is satisfied
    n = len(nums)
        
    # First, we convert the given array into a prefix sum array
    for i in range(1, n): nums[i] = nums[i - 1] + nums[i]
        
    # The prefix sum array will help in such a way that
        
    # Suppose the "left" subarray ends at index "left"
    # Suppose the "mid" subarray starts at index "left + 1" and ends at index "mid"
    # And finally, suppose the "right" subarray starts at index "mid + 1" and ends at index "right"

    # To find the sum of "mid" subarray, all we need to do is nums[mid] - nums[left]
    # To find sum of "left" subarray, we just do nums[left]
    # To find sum of "right" subarray, we just do nums[right] - nums[mid]
        
    # For every i (index where "left" subarray ends)
    for i in range(0, n):
        # Each "j" index is the index at which "mid" subarray ends
        for j in range(i + 1, n):
            leftSubarraySum = nums[i]
            midSubarraySum = nums[j] - nums[i]
            rightSubarraySum = nums[n - 1] - nums[j]
            if (leftSubarraySum <= midSubarraySum) and (midSubarraySum <= rightSubarraySum): 
                ways += 1
        
    return ways % 1000000007

nums = [1,2,2,2,5,0]

print("Ways to Split -> ", waysToSplit(nums))