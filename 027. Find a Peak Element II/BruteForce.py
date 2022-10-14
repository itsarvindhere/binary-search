# Helper method to check if an element is peak element or not
def isPeak(mat, row, col, m, n):
    # Check if it is greater than left neighbor
    if col > 0 and not (mat[row][col] > mat[row][col - 1]): return False
                
    # Check if it is greater than right neighbor
    if col < n - 1 and not (mat[row][col] > mat[row][col + 1]): return False
                    
    # Check if it is greater than top neighbor
    if row > 0 and not (mat[row][col] > mat[row - 1][col]): return False
                    
    # Check if it is greater than bottom neighbor
    if row < m - 1 and not (mat[row][col] > mat[row + 1][col]): return False
                    
    # If we are here, then this means, this element is the peak element
    return True
    
    
    
def findPeakGrid(mat):  
    m = len(mat)
    n = len(mat[0])
        
    for row in range(m):
        for col in range(n):
			# if this element is the peak element, stop and  return the indices
            if isPeak(mat, row, col, m, n): return [row,col]


mat = [[1,4],[3,2]]
print("Peak Element Position is -> ", findPeakGrid(mat) )