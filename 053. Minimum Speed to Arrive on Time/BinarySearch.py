# Helper method to check if a particular speed value is valid as per problem
from math import ceil
def isValid(speed, dist, hour):
    timeTaken = 0
        
    for i in range(len(dist) - 1): timeTaken += ceil(dist[i] / speed)
            
    # Last train
    timeTaken += dist[-1] / speed
            
    return timeTaken <= hour
    
    
    
def minSpeedOnTime(dist, hour):
    # Since we are asked for minimum Speed
    # We can apply Binary Search on Answer
        
    # What can be the range of speed for any input?
    
    # What can be the minimum possible speed?
    # Since "hour" can be at least 1
    # And distance can be at least 1
    # It means, minimum speed can be 1 too
    start = 1
        
    # What can be the maximum speed of any input?
    # It is given that answer will not exceed 10^7 so we can take that as max speed here
    end = pow(10, 7)
        
    minSpeed = -1
    while start <= end:
        mid = start + (end - start) // 2
            
        # If "mid" speed is valid, that is one possible solution
        # But we are asked for "minimum" speed
        # Hence, we try to search for a smaller "valid" speed than mid
        # That is, search on left side of mid
        if isValid(mid, dist, hour):
                minSpeed = mid
                end = mid - 1
            
        # If "mid" speed is not valid, that simply means, no speed less than mid can be valid too
        # So, no need to search on left side of mid as all values are invalid. 
        # Hence, search on right side of mid
        else: start = mid + 1
        
        
    return minSpeed

dist = [1,3,2]
hour = 6


print("Minimum Speed to Arrive on Time -> ", minSpeedOnTime(dist, hour), "km/h")