def mySqrt(x):
    for i in range(0, x + 1):
        # If square of current number gives us x 
        if i * i == x: return i
        # If square of current number gives us value more than x
        # That means, return the previous number since x is not perfect square
        if i * i > x: return i - 1
            
    return -1

x = 8
print("Square Root is ->", mySqrt(x))