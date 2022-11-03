from math import sqrt
def judgeSquareSum(c):
    # Since we want two numbers "a" and "b" such that 
    # a^2 + b^2 = c
        
    squareRoot = int(sqrt(c))
        
    # For every possible value of "a"
    for a in range(0, squareRoot + 1):
        # Instead of linear scan, we can try Binary Search as range is in sorted order
        start = 0
        end = squareRoot + 1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            value = (a * a) + (mid * mid)
                
            # If b = mid then, if condition is satisfied
            # We found a pair
            if value == c: return True
                
            # If the value becomes more than "c", then we need to decrease value of "b"
            # Because "a" is constant in this while loop and only "b" can change
            if value > c: end = mid - 1
                    
            # If the value becomes less than "c", then we need to increase value of "b"
            else: start = mid + 1

    # If we come out of the loop, that means no pair exists
    return False

c = 5
print("Output -> ", judgeSquareSum(c))