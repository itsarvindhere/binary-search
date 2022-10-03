def isPerfectSquare(num):
    if num == 1: return True
    # For any number > 1, its square root can lie between 1 to half of that number
    # So we will apply Binary Search on range 1 to n/2
    start = 1
    end = num // 2
        
    while start <= end:
        mid = start + (end - start) // 2
        square = mid * mid
        # If square of mid is equal to number, that means, number is a perfect square
        if square == num : return True
        # If square of mid is less than number, that means, we need a bigger value
        # So move to right of mid
        if square < num: start = mid + 1
        # If square of mid is greater than number, that means, we need a smaller value
        # So move to left of mid
        else: end = mid - 1
        
    # Not a perfect Square
    return False

num = 16
print("Output -> ", isPerfectSquare(num))