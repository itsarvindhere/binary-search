def chalkReplacer(chalk, k):
    totalSum = sum(chalk)
        
    # The reason why above approach fails is because of the value of "k"
    # Since it can be huge, we have to iterate through the array again and again
    # Until we make it so small that our condition fails
    # But what if we can bring the value of "k" down such that we can find the required index in just one pass?
        
    # If we reach last index and k is still larger, we have to again start from beginning
    # This means, in one loop, we will reduce k by sum of the array.
    # So to avoid this loop again ang again, we can do ->  k mod total sum of the array. 
    # In this way, we can find the required index in O(N) time
    k = k % totalSum
        
    n = len(chalk)
        
    # Now, we can find the required index in just O(n) time
    for i in range(n):
        if chalk[i] > k: return i
        k -= chalk[i]
            
    return 0

chalk = [3,4,1,2]
k = 25

print("Student that will replace chalk -> ", chalkReplacer(chalk, k))