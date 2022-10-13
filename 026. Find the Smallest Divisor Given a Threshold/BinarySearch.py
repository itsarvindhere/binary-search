# Helper Method to check if a particular value can be a valid divisor
from math import ceil
def isValid(val, nums, threshold):
        
    sum = 0
        
    # Get the sum
    for num in nums: sum += ceil(num/val)
    
    # It is a valid value if the sum of less than or equal to threshold
    return sum <= threshold

    
def smallestDivisor(nums, threshold):
    # Binary Search on Answer
        
    # We are asked for the smallest divisor
    # What can be the range of possible divisors?
        
        
    # It can be at least 1
        
    # If we take any number that is greater than any value in list
    # Then we will always get the same result
    # So it makes sense to choose the upper limit of the divisor as the maximum value in the list
        
    start = 1
    end = max(nums)
        
    # Result is the divisor we want to return
    # We want to minimize this result 
    # i.e., smallest possible divisor that satisfies the condition
    result = -1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # Check if "mid" value as divisor satisfies the conndition
        # If yes, that means, all values bigger than it will also satisfy
        if isValid(mid, nums, threshold):
            # So it is one possible solution
            result = mid
            # Since we want to minimize the divisor
            # we keep searching on left of mid
            end = mid - 1
        # If "mid" value as divisor does not satisfy the condition
        # no value less than mid will satisfy
        # So search for a valid value on right side of mid
        else: 
            start = mid + 1
                
    return result


nums = [44,22,33,11,1]
threshold = 5

print("Smallest Divisor is -> ", smallestDivisor(nums, threshold))