def chalkReplacer(chalk, k):

    k %= sum(chalk)
        
    # Since this problem is also tagged under Binary Search, how can we use binary search here?
    # Look what we are doing in above approach. 
    # We are reducing k by chalk[i] until k becomes less than any chalk[i]
        
    # At index = 0, we do k - chalk[0]
    # At index = 1, we do k - chalk][0] - chalk[1]
    # At index = 2, we do k - chalk][0] - chalk[1] - chalk[2]
        
    # In other words we are doing -> k - (chalk][0] + chalk[1] + chalk[2])
        
    # So, if we calculate the prefix sum of this array, 
    # then all that's left to find is at what index, the value is > k
        
    # Lets convert this chalk array to a prefix sum array
    # And since it is a prefix sum array, it means this will also be a sorted array
    # As each value is >= previous value
    n = len(chalk)
    for i in range(1, n): chalk[i] = chalk[i] + chalk[i - 1]
            
    # Binary Search to find the "first" index at which value > k
    # Note that we have to find the "first" index at which value > k
    # It means even if mid is the index at which value > k, we have to keep searching on left of mid
    start = 0
    end = n - 1
    index = 0
        
    while start <= end:
        mid = start + (end - start) // 2
            
        if chalk[mid] > k:
            index = mid
            end = mid - 1
        else: start = mid + 1

    return index

chalk = [3,4,1,2]
k = 25

print("Student that will replace chalk -> ", chalkReplacer(chalk, k))