# Helper method to find if we can run "n" computers simultaneously for "x" minutes
def isValid(x, n, batteries):
    runningTime = 0
        
    for minute in batteries:
            
        # If a battery has at least "x" minutes of charge 
        # Then we use only "x" minutes from it
        # Otherwise, we use that battery fully
        runningTime += min(minute, x)
        
    # How many computers can we run with this running time?
    computers = runningTime / x
        
    # If number of computers we can run is at least "n" then it means "x" is valid
    return computers >= n
        
    
def maxRunTime(n, batteries):
    # We have to find the Maximum Running time
        
    # What can be the lower bound of Running time?
    # What is there is only one computer and only one battery with 1 minute of charge
    # In that case, we can only run the computer for 1 minute
    start = 1
        
    # What can be the upper bound?
    end = sum(batteries) // n
        
    maxTime = 1
        
    # And now, in this range, we have to find the maximum running time
    # We can use Binary Search here because not only this range is in sorted order
    # But there is also monotonicity
        
    # If we can run "n" computers for "x" minutes simultaneously
    # Then ofcourse, we can also run them for less than "x" miniutes simultaneously
        
    # Similarly, If we can not run "n" computers for "x" minutes simultaneously
    # No value more than "x" can be valid
        
    while start <= end:
        mid = start + (end - start) // 2
            
        if isValid(mid, n, batteries):
            maxTime = mid
            start = mid + 1
        else: end = mid - 1

    return maxTime


batteries = [2,3,2,1,7,8,2,4]
n = 4

print("Maximum Running Time -> ", maxRunTime(n, batteries))