def findPairs(nums, k):
    dict = {}
    pairs = 0
        
    # First, keep the count of each number in the dictionary
    for num in nums: dict[num] = dict[num] + 1 if num in dict else 1
            
    # Now, for every element/key (since keys are unique so it will ensure pairs are unique)
    # This will also ensure that we do not have to manually decrease count of a number 
    # In case k == 0. Because we will traverse each number only once as keys are unique
    for num in dict:
        # It is possible that k is 0 for example, we may have two 1s in array and k = 0
        # So in that case, a valid pair will be (1,1)
        # So for such cases, we have this condition where we check 
        # if we have more than one occurance of that number
        condition1 = (k == 0 and dict[num] > 1)
            
        # Otherwise, we just check if (first number + k) is present in dictionary or not
        # As we know, lookup is a O(1) operation in a dictionary
        condition2 = (k > 0 and (num+k in dict))
            
        if condition1 or condition2: pairs += 1
            
        
    return pairs


nums = [3,1,4,1,5]
k = 2

print("Number of K-diff Pairs -> ", findPairs(nums, k))