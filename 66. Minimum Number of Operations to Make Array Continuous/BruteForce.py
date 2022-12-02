def minOperations(nums):
    n = len(nums)
    # Since we want to convert "nums" into a continuous array
    # It means, it will not have any duplicates
    # So first, we will remove the duplicates
        
    nums = set(nums)
        
    maxReusedElements = 1
        
    for num in nums:
        reused = 0
        # If we consider "num" to be the minimum in resulting continous array
        # Then we know the maximum element in that array needs to be "num + n - 1"
        # So now we want to check how many elements we can reuse
        for i in range(num, num + n):
            if i in nums: reused += 1
                    
        maxReusedElements = max(maxReusedElements, reused)
            
    return n - maxReusedElements

nums = [1,10,100,1000]

print("Minimum Number of Replacements -> ", minOperations(nums))