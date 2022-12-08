def minOperations(nums):
    n = len(nums)
    # Since we want to convert "nums" into a continuous array
    # It means, it will not have any duplicates
    # So first, we will remove the duplicates
        
    nums = list(set(nums))
        
    # To use Sliding Window, we also Sort this array
    nums.sort()
        
    maxReusedElements = 1
    i,j = 0,0
        
    while j < len(nums):
            
        # While this window is valid, keep increasing its size from right end
        # And also keep track of the maximum window size
        # Because that refers to number of elements we can reuse
        while j < len(nums) and nums[j] <= nums[i] + n - 1: 
            maxReusedElements = max(maxReusedElements, j - i + 1)
            j += 1
            
        # Shrink the window from left end
        i += 1

    return n - maxReusedElements

nums = [1,10,100,1000]

print("Minimum Number of Replacements -> ", minOperations(nums))