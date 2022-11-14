# Helper method to find if each child can get "x" candies
def isValid(x, candies, k):
    children = 0

    for pile in candies: 
        children += int(pile / x)
                            
        # No need to go in further iterations if this is the case
        if children >= k: return True
                
    return children >= k

def maximumCandies(candies, k):
        
    # We want to find the maximum number of candies each child can get
    # Now, let's try to figure out what is the range of possible valid values for number of candies
        
    # A child may get no candy at all. So minimum possible value is 0
    start = 0
        
    # A child may get the whole pile. And since it is given that a child can take at most a pile
    # Maximum possible value is maximum candies in any pile
    end = max(candies)

    # And now, in this range, we want to find the maximum candies each child can get

    # One thing to note is that, if each child can get "x" candies, 
    # then each child can get any number of candies less than x as well
    # So there is monotonicity
    # And hence, on this range (which is sorted) we can apply Binary Search to find maximum valid value
    maxCandies = 0
            
    while start <= end:
        mid = start + (end - start) // 2
            
        if mid == 0 or isValid(mid, candies, k):
            maxCandies = mid
            start = mid + 1
        else: end = mid - 1
                
    return maxCandies


candies = [5,8,6]
k = 3

print("Output -> ", maximumCandies(candies, k))