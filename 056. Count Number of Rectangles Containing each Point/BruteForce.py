def countRectangles(rectangles, points):
    # Output array to return
    count = []
    
    # For each point
    for point in points:
        # Go through each rectangle and check if this point lies in this rectangle or not
        rectCount = 0
        for rectangle in rectangles:
            # If this rectangle contains this point, increment the count for this point
            if point[0] <= rectangle[0] and point[1] <= rectangle[1]: rectCount += 1
        
        # And append the count we get after the above loop in the final output array
        count.append(rectCount)
        
    return count

rectangles = [[1,2],[2,3],[2,5]]
points = [[2,1],[1,4]]

print("Output -> ", countRectangles(rectangles, points))