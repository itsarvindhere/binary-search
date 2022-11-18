# Helper method to check if "x" can be the minimum possible value of the maximum integer of nums
# "x" can be the minimum possible value if after performing any number of operations if
# The maximum value at the end of resultinng array is <= x
# So in short, we are trying to take each value and make sure it is <= x
# If it is more than "x", then when we reduce it, we also want to increment the previous value by the same amount
def isValid(x, nums): 
    buffer = 0
        
    for num in nums:
        # If num is less than x, that means, we have a buffer of (x - num)
        # So we can increment this value by atmost (x - num)
        if num < x: 
            buffer += x - num
        else:
            # If num is greater than x, we have to decrement it
            # But we only can use the available buffer
            # That is, the amount by which we have to decrement, should be <= buffer
            buffer -= num - x
            if buffer < 0: return False

    return True
                
    
def minimizeArrayValue(nums):
    # We want to find minimum possible value of the maximum number in the list
    # What can be the range?
        
    # Ofcourse, we are trying to reduce the maximum value which means upper limit is the maximum value itself
        
    # What can be the smallest possible valid value after reducing the maximum number?
    # So we can take "0" as the lower limit since nums[i] can be at least 0
        
    start = 0
    end = max(nums)

    minValue = end
        
    # For cases like [10, 0] where 0th index has the maximum value
    if nums[0] == end: return minValue

    while start <= end:
        mid = start + (end - start) // 2
            
        # If "mid" can be the minimum value of the maximum integer of nums
        # Then that means any value more than "mid" is also valid
        # but we want to minimize this value so we keep searching on left side of mid
        if isValid(mid, nums):
            minValue = mid
            end = mid - 1
            
        # If "mid" cannot be the minimum value, no value less than "mid" is valid
        # Hence, we will search for a valid minimum possible value on the right side of mid
        else: start = mid + 1
        
    return minValue

nums = [3,7,1,6]

print("Minimum Possible Value -> ", minimizeArrayValue(nums))