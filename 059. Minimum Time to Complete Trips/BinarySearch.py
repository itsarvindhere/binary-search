# Helper method to check if all buses can complete at least "totalTrips" in "x" time
def isValid(x, time, totalTrips):
    trips = 0
        
    for t in time: 
        # If a bus takes "t" time to complete 1 trip
        # Then in "x" time, it will complete "x/t" trips
        trips += int(x/t)
            
        # If already we have completed at least "totalTrips" we can return True here itself
        if trips >= totalTrips: return True
        
    return False
    
def minimumTime(time, totalTrips): 
    # Binary Search on Answer
        
    # We are asked for the minimum time required for all the buses to complete at least totalTrips
    # Now, what can be the lower bound of minimum time. That is, the smallest possible valid value
        
    # It can be the smallest time in the list. For example, time = [2] and totalTrips = 1
    # In this case, the minimum time is "2" as there is only one bus and it will complete its 1 trip at t = 2
        
    # And similarly, what can be the upper bound? That is, the largest possible valid value
    # Since both totalTrips and time[i] can be up to 10^7
    # It means it is also possible that we have a test case like : time = [10^7] and totalTrips = 10^7
    # In that case, the output will be 10^14. Why? Because in this case, a bus takes 10^7 time to complete 1 trip
    # Which means, to complete 10^7 trips, it will take (10^7 * 10^7) time => 10^14 time
    # and that's the largest possible value for the time taken to complete at least totalTrips
        
    start = min(time)
    end = 10**14
        
    minTime = 0
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If all buses can complete at least "totalTrips" in "mid" time
        # Then this is one possible solution
        # But since we have to mninimize this time, we will keep searching on left side of mid
        if isValid(mid, time, totalTrips):
            minTime = mid
            end = mid - 1
            
        # If all buses can not complete at least "totalTrips" in "mid" time
        # There is no need to look at left side of mid as all values to left will also not be valid
        # Hence, in that case, search on right side of mid
        else: start = mid + 1

    return minTime

time = [1,2,3]
totalTrips = 5

print("Minimum Time to Complete at least", totalTrips , "Trips -> ", minimumTime(time, totalTrips))