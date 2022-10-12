from sortedcontainers import SortedList 
events = SortedList()

def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        if arr[mid] < target: start = mid + 1
        else: end = mid - 1
        
    return start

def book(start, end):

    startIndex = binarySearch(events, start)
    endIndex = binarySearch(events, end)
        
    # An event does not intersect any other event if - 
    #      The ideal index of "start" value in list is even
    # AND   The ideal index of "start" is equal to "end"

    if not ((startIndex == endIndex) and (startIndex % 2 == 0)): return False
        

    # If we are at this line, that means we can book this event so return True
    # Also, insert he start and end values for this event in the list
    events.add(start)
    events.add(end - 1)
    return True



print("Can we book start = 10 and end = 20 -> ", book(10,20))
print("Can we book start = 15 and end = 20 -> ", book(15,20))
print("Can we book start = 25 and end = 30 -> ", book(25,30))