# Helper Method to check if a value is a valid magnetic force value between any two balls
def isValid(magneticForce, m, position):
    # Keep first ball at first place so we can start with at least one ball
    balls = 1
    prevPos = position[0]
        
    for i in range(1, len(position)):
        # If magnetic force between current basket and basket of previous ball is at least equal to "magneticForce"
        # That means we can place a ball in this position
        if position[i] - prevPos >= magneticForce:
            balls += 1
            prevPos = position[i]
            
    # If we can place at least "m" balls with magnetic force at least equal to "magneticForce" between any two balls
    # Then return True
    # Else return False
    return balls >= m
        
    
    
    
def maxDistance(position, m):
    # Binary Search on Answer
        
    # Here, we are asked to maximize the minimum magnetic force between two balls
        
    # So, lets see what is the range of possible magnetic force values
        
    # It can be at least 1. Suppose there are same number of balls as the baskets
    # In that case, we will have to place each ball next to one another
        
    # What can be the maximum possible magnetic force value?
    # Suppose we have only two balls. What is the maximum? We can place both at two ends of the array if array is sorted
    # Which means magnetic force will be (rightmost value - leftmost value) of sorted array
        
    # And that's it. Our possible solutions will be in this range only
    # Because it is not given that the array will be sorted, we will need to sort it first
        

    position.sort()
        
    start = 1
    end = position[-1] - position[0]
        
    # If there are two balls, we can simply return the difference between last and first value
    if m == 2: return end
        
    # We want to maximize this result
    result = -1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # Now we need to check, can we put balls in baskets
        # such that magnetic force between two balls is at least "mid"
        if isValid(mid, m, position):
            # If mid is valid, all values before it are also valid
            # And since we want to maximize we keep searching on right side
            result = mid
            start = mid + 1
        # If we cannot have a magnetic force at least "mid" between any two balls,
        # any value more than mid is also not valid
        # So search for a valid value on the left side of mid
        else: end = mid - 1
        
        
    return result

position = [1,2,3,4,7]
m = 3

print("Force -> ", maxDistance(position, m))