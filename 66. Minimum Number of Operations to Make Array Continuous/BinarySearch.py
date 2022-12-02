def minOperations(nums):
    n = len(nums)
    # Since we want to convert "nums" into a continuous array
    # It means, it will not have any duplicates
    # So first, we will remove the duplicates
        
    nums = list(set(nums))
        
    # To use Binary Search, we also Sort this array
    nums.sort()
        
    maxReusedElements = 1
        
    for i,num in enumerate(nums):
        # This time, instead of linear search, we will do Binary Search
        # Because since array is sorted, we just want to find the largest element in array that is <= num + n - 1
        # And the number of elements in between = number of elements we can reuse 
            
        # Note that here, we are not using "n" which is the old length before we removed duplicates
        # Here we are using len(nums) that is, the new length of the list after removing duplicates
        start = i
        end = min(i + len(nums) - 1, len(nums) - 1)
            
        rightmostIndex = i
            
        while start <= end:
            mid = start + (end - start) // 2
                
            # Here we are using "n" which is the length of original array
            # Since the final continous array needs to be of length "n"
            if nums[mid] <= num + n - 1:
                rightmostIndex = mid
                start = mid + 1
            else: end = mid - 1
            
        maxReusedElements = max(maxReusedElements, rightmostIndex - i + 1)
        
    # Now that we have the Maximum number of elements we can reuse
    # Just return the minimum replacements we need to make
    return n - maxReusedElements

nums = [1,10,100,1000]

print("Minimum Number of Replacements -> ", minOperations(nums))