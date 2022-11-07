def findPairs(nums, k):
    # Becase we want unique pairs only, we will use a set to keep the unique pairs
    pairs = set()

    n = len(nums)
        
    # Next, for each element, we do a Linear Search for the second element
    for i in range(n):
        for j in range(n):
            if i != j and nums[i] - nums[j] == k:
                pairs.add(nums[i])
                    
    # And as we have to return how many unique pairs are there
    # We will return the size of the Set
    return len(pairs)


nums = [3,1,4,1,5]
k = 2

print("Number of K-diff Pairs -> ", findPairs(nums, k))