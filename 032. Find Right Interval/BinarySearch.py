# Binary Search for the smallest "start" interval value that is >= "target"
def binarySearch(intervals, target, indices):
    start = 0
    end = len(intervals) - 1
    result = -1
            
    while start <= end:
        mid = start + (end - start) // 2
                
        if intervals[mid][0] >= target:
            # Get the index of this interval in the original list (before sorting)
            # And set that as the value of "result"
            result = indices[intervals[mid][0]]
            end = mid - 1
        else: start = mid + 1
        
    return result

    
def findRightInterval(intervals):
    output = [-1] * len(intervals)
        
    # It is given that "start" is unique for each interval
    # We can use that to store the index of each start value in a map
    indices = {}
        
    # We do this because later on, we are going to sort the list
    # But in the result list, we want the original index values
    for i,interval in enumerate(intervals): indices[interval[0]] = i
            
    # Sort the Intervals list
    intervals.sort()
        
    for interval in intervals:
        # The index of this interval in original list before we sorted it
        startIndex = indices[interval[0]]
            
        # We want a smallest start value that is >= target
        # In other words, we want the ceil value of target in intervals
        target = interval[1]
            
        result = binarySearch(intervals, target, indices)
            
        output[startIndex] = result
            
                
    return output


intervals = [[3,4],[2,3],[1,2]]

print("Output List is -> ", findRightInterval(intervals))