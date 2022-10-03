def isPerfectSquare(num):
    if num == 1: return True
        
    # Go through each number from 1 to half of input number
    # And check if its square is equal to num
    for i in range(1, num + 1):
        if i * i == num: return True
        # Not a perfect square
        # Don't waste time checking for numbers greater than i
        # Return from here itself
        if i * i > num: return False
        
    return False