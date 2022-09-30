def countNegatives(grid):
    # To store the count of negatives
    count = 0
        
    # m = Rows
    # n = Columns
    m = len(grid)
    n = len(grid[0])
        
    # The element at the last row and last column is the smallest element in matrix
    # If that element is not negative, then that means there is no negative element at all
    if grid[m-1][n-1] >= 0: return 0

        
    # Similarly, The element at the first row and first column is the largest element in matrix
    # If that element is negative, then that means all elements are negative
    if grid[0][0] < 0: return m * n
        
    # Start from bottom left corner
    # Why? Because all element on top are bigger and all elements on right side are smaller
	# So as soon as we find a negative element
	# We know all elements after this element in current row are negative
        
    start = m-1
    end = 0
        
    while start >= 0 and end < n:
		# If element is negative, all elements after it are negative
		# So increment count and move to previous row
        if grid[start][end] < 0: 
            count += n - end
            start -= 1
		# Otherwise move to next column to search for a negative number
        else:
            end += 1
        
        
    return count


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

print("Count of Negative Numbers ->", countNegatives(grid))