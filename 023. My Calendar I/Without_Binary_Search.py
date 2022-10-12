events = []
def book(start, end):
    # If there are events, check if new event intersects any previous event
    for event in events: 
        # At each index we have a tuple
        # first element of tuple represents start of event
        # second element of tuple represents end of event
        prevStart = event[0]
        prevEnd = event[1]
            
        # Check for intersection
        # An event is not intersecting if - 
        #    it starts after the end of any previous event
        # or it ends before the starting of any previous event
            
        # If the above condition is not satisfied, there is an intersection
        if not(start > prevEnd or (end - 1) < prevStart): return False
            

    # If we are at this line, that means we can book this event so return True
    events.append((start, end - 1))
    return True



print("Can we book start = 10 and end = 20 -> ", book(10,20))
print("Can we book start = 15 and end = 20 -> ", book(15,20))
print("Can we book start = 25 and end = 30 -> ", book(25,30))