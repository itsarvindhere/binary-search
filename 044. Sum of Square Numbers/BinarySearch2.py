from math import sqrt
def judgeSquareSum(c):
    # Since we want two numbers "a" and "b" such that 
    # a^2 + b^2 = c
        
    squareRoot = int(sqrt(c))
        
    # For every possible value of "a"
    for a in range(0, squareRoot + 1):
        # Instead of linear scan, we can try Binary Search as range is in sorted order
        # When we are here, we have "a" value and "c" value. So all that we are looking for is the "b" value
            
        # a^2 + b^2 = c
        # From this, b^2 = c - a^2
        # Or, b = sqrt(c - a^2)
            
            
        # So this is the value we need to search for in the range 0 to sqrt(c)
        target = sqrt(c - (a * a))
            
            
        start = 0
        end = squareRoot
            
        while start <= end:
            mid = start + (end - start) // 2
                
            if mid == target: return True
                
            if mid > target: end = mid - 1
            else: start = mid + 1

    # If we come out of the loop, that means no pair exists
    return False

c = 5
print("Output -> ", judgeSquareSum(c))