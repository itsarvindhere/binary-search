# Helper method to check if "x" can be a valid value at nums[index]
# That is, whether we can generate a valid array with nums[index] == x
def isValid(x, n, index, maxSum):
        
    leftSum, rightSum = 0,0
        
    # How many elements are there on right side of "index"? 
    # It is (n - index - 1)
    elementsOnRight = n - index - 1
        
    # If we do not have to add any extra 1s
    if elementsOnRight < x:
        # First calculate sum from 1 to "x - 1" value
        rs1 = (x - 1) * ((x - 1) + 1) // 2
            
        # Next, calculate sum from 1 to "x - elementsOnRight - 1" value
        rs2 = (x - elementsOnRight - 1) * ((x - elementsOnRight - 1) + 1) // 2
            
        # And now, right side sum is the difference between rs1 and rs2
        rightSum = rs1 - rs2
        
        
    # If we have to add extra 1s
    else:
            
        # First calculate sum from 1 to "x - 1" value
        rs1 = (x - 1) * ((x - 1) + 1) // 2
            
        # We have to add how many extra 1s?
        rs2 = (elementsOnRight - x) + 1
            
        rightSum = rs1 + rs2
            
        
    # Now we have to do the similar thing with "left" side sum
    # How many spaces are there to fill on left side of "index"?
    # It will be "index" itself because array is 0-indexed
    elementsOnLeft = index
        
    # If we do not have to add extra 1s
    if elementsOnLeft < x:
        # Same thing as rightSum now
            
        # First calculate sum from 1 to "x - 1" value
        ls1 = (x - 1) * ((x - 1) + 1) // 2
            
        # Next, calculate sum from 1 to "x - elementsOnLeft - 1" value
        ls2 = (x - elementsOnLeft - 1) * ((x - elementsOnLeft - 1) + 1) // 2
            
        # And now, left side sum is the difference between ls1 and ls2
        leftSum = ls1 - ls2
            
    else:
            
        # First calculate sum from 1 to "x - 1" value
        ls1 = (x - 1) * ((x - 1) + 1) // 2
            
        # We have to add how many extra 1s?
        ls2 = (elementsOnLeft - x) + 1
            
        leftSum = ls1 + ls2
        
    totalSum = leftSum + rightSum + x
        
    return totalSum <= maxSum
    
    
    
def maxValue(n, index, maxSum):
    # BINARY SEARCH ON ANSWER
        
    # We want to maximize nums[index]
        
    # What can be the lower bound of nums[index]?
    # Since all numbers are positive numbers in nums, nums[index] can be at least 1
        
    # What can be the upper bound of nums[index]?
    # Since we want to ensure that sum does not exceed maxSum
    # It means, nums[index] can be at most maxSum.
        
    start = 1
    end = maxSum
        
    maxVal = 1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If nums[index] can have "mid" value and all conditions are satisfied
        # Then this is one possible solution
        # But since we want to maximize nums[index]
        # We keep searching for a higher valid value on right side of mid
        if isValid(mid, n, index, maxSum):
            maxVal = mid
            start = mid + 1
        # If nums[index] cannot have "mid" value
        # Then no value higher than "mid" will be valid
        # So in that case, we will search for a value smaller than mid
        # Hence, search on left side of mid
        else: end = mid - 1
                
    return maxVal

n = 4
index = 2
maxSum = 6

print("Maximum Value at index", index, "is -> ", maxValue(n, index, maxSum))
