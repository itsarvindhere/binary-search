# Helper method to check whether a particular capacity is valid 
# It is valid if we can ship all packages withing given number of days
    
def canShip(capacity, days, weights):
    dayCount = 1
    currWeight = 0
        
    for weight in weights:
        currWeight += weight
        if currWeight > capacity:
            dayCount += 1
            if dayCount > days: return False
            currWeight = weight
        
    return True
    
    
def shipWithinDays(weights, days):
    # We are asked to find the minimum weight capacity
    minimumCapacity = 0
        
    # We can apply Binary Search on the range of a possible solutions
    # What can be the least weight capacity? It can be the maximum weight in array
    # And what can be the highest weight capacity? It can be the sum of all the weights
    # That is, ship might be capable of shipping all the packages at once
        
    # So we need to Binary Search this range for the minimum weight capacity such that all the packages
    # are shipped within 'days' days
    start = max(weights)
    end = sum(weights)
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If we can ship all packages within "days" days with weight capacity = mid
        # That means it is one possible solution
        # Since we want minimum, continue searching on left of mid
        if canShip(mid, days, weights):
            minimumCapacity = mid
            end = mid - 1
        # If we cannot ship all packages within "days" days with weight capacity = mid
        # This means any value less than mid is obviously not valid too
        # So search on right side of mid for a valid value
        else: start = mid + 1
                
    return minimumCapacity


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print("Minimum Capacity -> ", shipWithinDays(weights, days))