def findPairs(nums, k):
    # Becase we want unique pairs only, we will use a set to keep the unique pairs
    pairs = set()
        
    # First, we sort the list
    nums.sort()
        
    n = len(nums)
        
    # Next, for each nums[j], we Binary Search for the nums[i]
    for j in range(n):
        start = j + 1
        end = n - 1
        target = k + nums[j]
            
        while start <= end:
            i = start + (end - start) // 2
                
            if nums[i] == target: 
                pairs.add(nums[j])
                break
            if nums[i] < target: start = i + 1
            else: end = i - 1       
        
        
    # And as we have to return how many unique pairs are there
    # We will return the size of the Set
    return len(pairs)


nums = [3,1,4,1,5]
k = 2

print("Number of K-diff Pairs -> ", findPairs(nums, k))