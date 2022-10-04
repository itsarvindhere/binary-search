def mySqrt(x):
    # For x = 0 and x = 1
    if x <= 1: return x
        
    start = 2
    # We know that a square root of any number is at most the mid, not more than that
    end = x // 2
        
    # Apply Binary Search since range 1 to x is in sorted order
    while start <= end:
        mid = start + (end - start)  // 2
            
        square = mid * mid
        # If square of a number is equal to x, we got the square root
        if square == x: return mid
        # If square of a number if less than x, go for a bigger number
        if square < x: start = mid + 1
        # If square of a number if more than x, go for a smaller number
        else: end = mid - 1
        
    # If the number is not a perfect square, return the value "end"
    return end


x = 8
print("Square Root is ->", mySqrt(x))