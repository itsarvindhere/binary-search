from math import sqrt
def judgeSquareSum(c):
    # Since we want two numbers "a" and "b" such that 
    # a^2 + b^2 = c
        
    # So, these two numbers should be in the range -> 0 to square root of "c"
    squareRoot = int(sqrt(c))
        
    # In Brute Force Approach, for every possible value of "a"
    for a in range(0, squareRoot + 1):
        # We need to go through every possible value of "b"
        for b in range(0, squareRoot + 1):
            # If we find a pair, then return True
            if (a * a) + (b * b) == c: return True
        
        
    # If we come out of the loop, that means no pair exists
    return False

c = 5
print("Output -> ", judgeSquareSum(c))