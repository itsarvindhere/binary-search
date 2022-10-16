from math import ceil
# Helper Method to check if koko can eat all the bananas in "h" hours
# With a per-hour eating speed of "k"
def isValid(k, piles, h):
    hoursTaken = 0
        
    for pile in piles:
        # How many hours Koko will take to eat all bananas from this pile
        hoursTaken += ceil(pile/k)
    
        # Invalid "k" speed
        # Because we want Koko to finish all piles in hoursTaken <= h 
        if hoursTaken > h: return False

    return True
    
    
def minEatingSpeed(piles, h):
    # Binary Search on Answer
        
    # We have to return the "Minimum per-hour eating speed" k
    # Such that Koko can eat all the banans in "h" hours
        
    # What can be the lower bound of eating speed?
        
    # In other words, what can be the slowest eating speed?
    # It can be at least 1, that is, Koko can eat at least one banana each hour
    # In that case, she can finish each pile in "bananas in that pile" hours

    start = 1
        
    # Now think of the upper bound of eating speed
        
    # In other words, what can be the fastest eating speed?
    # Koko can only eat from one pile in an hour
    # So, the fastest speed will be the maximum number of bananas in any pile
    # Because in that case, she can finish each pile in an hour
        
    end = max(piles)
        

    # And we will find our solution in this range only
    minimumSpeed = 1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If Koko eats "mid" bananas per hour
        # And she can eat all bananas in "h" hours
        # Then that means, any value above "mid" is also valid
        # But we want the minimum valid value
        # Hence we search on the left side of mid
        if isValid(mid, piles, h):
            minimumSpeed = mid
            end = mid - 1
            
        # If she cannot eat all bananas in h hours with "mid" eating speed
        # Then no speed less than "mid" will be valid
        # So search on the right side of mid
        else: start = mid + 1
        
        
    return minimumSpeed

piles = [30,11,23,4,20]
h = 5

print("Minimum Eating Speed -> ", minEatingSpeed(piles, h))