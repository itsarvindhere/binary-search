from collections import defaultdict
def countRectangles(rectangles, points):
    # Output array to return
    count = []
        
    # Why did we get TLE in the above approach?
    # Because for every point, we have to traverse the array from the beginning to the end
        
    # First, let us sort the rectangles as per their lengths
    rectangles.sort()
        
    # The problem constrains say that height can be from 1 to 100
    # So we can track how many rectangles are there with a certain height
    dict = defaultdict(list)
        
    # For each height, we can keep the length of a rectangle in a corresponding list
    # Since we already sorted the rectangles list above by lengths, no need to worry about the order here
    for rectangle in rectangles: dict[rectangle[1]].append(rectangle[0])
        
    # Now, for each point
    for point in points:
        rectCount = 0
            
        # We know that point[1] is the "y" axis value of that point
        # So, any rectangle with height >= y should contain that point, right?
        # Given, the rectangle also has length >= point[0]
        for height in range(point[1], 101):
                
            # And now, we can apply Binary search to find the leftmost length of rectangle that contains this point
            # Once we find that, we know all lengths after that are also containing this point since list is sorted
            if height in dict:
                lengths = dict[height]
                    
                start = 0
                end = len(lengths) - 1
                leftmostIndex = -1
                    
                while start <= end:
                    mid = start + (end - start) // 2
                        
                    if lengths[mid] >= point[0]:
                        leftmostIndex = mid
                        end = mid - 1
                    else: start = mid + 1
                            
                if leftmostIndex != -1:
                    rectCount += len(dict[height]) - leftmostIndex
                    
        count.append(rectCount)
        
    return count

rectangles = [[1,2],[2,3],[2,5]]
points = [[2,1],[1,4]]

print("Output -> ", countRectangles(rectangles, points))