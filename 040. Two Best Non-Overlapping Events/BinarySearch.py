def maxTwoEvents(events):
    maxSum = 0
        
    n = len(events)
        
    # For Binary Search, we need Sorting first
    # If we apply sort method to events, it will sort the events based on start time
    events.sort()
        
    # Pre compute the maximum value on the right for each event
    maxOnRight = [0] * n
        
    # For last event, there is no event on its right
    # So for it, maximum is its value only
    maxOnRight[- 1] = events[-1][2]
        
    for i in range(n - 2, -1, -1): maxOnRight[i] = max(events[i][2], maxOnRight[i + 1])
        
    # For each event
    for i in range(n): 
        sum = events[i][2]
        maxVal = 0

        # Now, we can use Binary Search to find the leftmost valid event for ith event
        # Because if we can find such an index, then all events after that index are also valid
        # Because array is sorted based on start time 
        # so all events after that index will also have a start time greater than end time of ith event
        start = i + 1
        end = n - 1
        leftmostValid = -1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            # IF mid is a valid event that we can consider pairing
            # We can store this index as it may be the leftmost valid index
            # But we keep searching on left of mid to find the leftmost if there is any other valid event on left
            if events[mid][0] > events[i][1]:
                leftmostValid = mid
                end = mid - 1
                    
            # If mid itself is not valid, how can any event before mid can be valid?
            else: start = mid + 1      
                    
        # Now, all that we want is what is the maximum value in the [leftmostValid, n - 1] subarray
        # No need to find that again because we have precomputed that in the beginning
            
        if leftmostValid != -1: maxVal = maxOnRight[leftmostValid]
                
        maxSum = max(maxSum, sum + maxVal)
        
    return maxSum

events = [[1,3,2],[4,5,2],[1,5,5]]
print("Maximum Sum -> ", maxTwoEvents(events))