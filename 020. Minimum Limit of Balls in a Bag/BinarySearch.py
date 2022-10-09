# Helper Method to find if we can have a particular penalty
def isValid(penalty, nums, maxOperations):
        
    # Since penalty means maximum balls in a bag
    # For "penalty" to be a valid penalty, we need to make sure it is the largest value in the array
    # In other words, make sure every value is <= penalty
    # If any value is not <= penalty, we need to do some operations to make it <= penalty
    operations = 0
    for num in nums:
        if num > penalty:
                
            # How many opeartions are needed to convert this number into two numbers 
            # Such that the maxmimum of two numbers = penalty
            opsNeeded = num // penalty
                
            # If number is divisible by penalty, we need one less operation
            if num % penalty == 0: opsNeeded -= 1   

            operations += opsNeeded
                
            # If we have to do more than maxOperations, this is not a valid penalty value
            if operations > maxOperations: return False
                
    return True
    
    
def minimumSize(nums, maxOperations):
    # Binary Search on Answer

    # The answer is -> Minimum Penalty
        
    # What is penalty? It is the number of balls in a bag
    # So, we know that number of balls in any bag must lie in some particular range of values
        
    # It is given that a bag can have at least 1 ball. So that is the lower bound
    # And the upper bound is simply the maximum in the given array
        
    # So, the minimum penalty will lie between 1 to max in the array
        
    start = 1
    end = max(nums)
        
    minimumPenalty = -1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # mid is one possible penalty value
        # So we want to check can there be a penalty = mid for given array if we apply maxOperations
        # If yes, then this is one possible solution
        # But since we want to minimize the penalty, that means keep searching on left side of mid
        if isValid(mid, nums, maxOperations):
            minimumPenalty = mid
            end = mid - 1
                
        # If mid is not a valid penalty value for this array, no value before mid is valid
        # So search on right side of mid
        else: start = mid + 1
            
            
    return minimumPenalty



nums = [2,4,8,2]
maxOperations = 4
print("Minimum Possible Penalty is -> ", minimumSize(nums, maxOperations))