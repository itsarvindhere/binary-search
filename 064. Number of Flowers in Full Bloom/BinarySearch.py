def fullBloomFlowers(flowers, persons):
    output = []
    n = len(flowers)
        
    # Why did we get TLE in the Brute Force approach?
    # Because for each person, we have to traverse the whole flowers list
        
    # What if we sort the starting and ending time of flowers?
    startTime, endTime = [], []
        
    for flower in flowers:
        startTime.append(flower[0])
        endTime.append(flower[1])
            
    startTime.sort()
    endTime.sort()
        
        
    # Now, for each person's arriving time
    # Number of flowers blooming at that time = (Number of flowers that have started blooming - Number of flowers that have stopped blooming)
        
    for time in persons:
            
        # First, we Binary Search for how many flowers have already started blooming when time = "time"
        # That is, flowers for which startTime is <= "time"
        # If for a flower, startTime is <= time, then all flowers before it have also started blooming already
        # Hence, we are looking for rightmost flower for which startTime <= time
            
        start = 0
        end = n - 1
        startedBlooming = 0
            
        while start <= end:
            mid = start + (end - start) // 2
                
            if startTime[mid] <= time:
                startedBlooming = mid + 1
                start = mid + 1
            else: end = mid - 1
                    
        # Similarly, how many flowers have already stopped blooming when time = "time"
        # That is, flowers for which endTime is < time
        # So, if for a flower endTme is < time, we know all flowers before it have also stopped blooming already
        # Hence, we are looking for the rightmost flower for which endtime is < time
            
        start = 0
        end = n - 1
        stoppedBlooming = 0
            
        while start <= end:
            mid = start + (end - start) // 2
            if endTime[mid] < time:
                stoppedBlooming = mid + 1
                start = mid + 1
            else: end = mid - 1
            
        # Now, number of flowers that are blooming during time = "time" are
        count = startedBlooming - stoppedBlooming
            
        output.append(count)

    return output

flowers = [[1,6],[3,7],[9,12],[4,13]]
persons = [2,3,7,11]

print("Output -> ", fullBloomFlowers(flowers, persons))