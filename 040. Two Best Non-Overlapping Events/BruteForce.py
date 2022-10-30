def maxTwoEvents(events):
    maxSum = 0
        
    # For each event
    for i in range(len(events)): 
        sum = events[i][2]
            
        # Try to find the event that can be paired with it to get a maximum sum
        for j in range(len(events)):
            if i != j and events[j][0] > events[i][1]:
                maxSum = max(maxSum, sum + events[j][2])            
            
        # This is for the cases when we cannot find any other event with which this event can be paired
        # It is also possible that a single event has a higher value than any other valid pair combined
        maxSum = max(maxSum, sum)
    return maxSum

events = [[1,3,2],[4,5,2],[1,5,5]]
print("Maximum Sum -> ", maxTwoEvents(events))