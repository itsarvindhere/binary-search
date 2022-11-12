def hIndex(citations):
    # The problem asks us to write a logarithmic time solution
    # Which means, we have to use Binary Search only once, not nested Binary search as in above approach
    # This should result in an overall time complexity of O(LogN) which makes it the fastest solution than all 
        
    n = len(citations)
    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
			
		# Suppose h = citations[mid]
		# Now, if number of papers with citation >= h is exactly equal to h
		# What that means? That means, the optimal answer is the current "h" only
		# Because that's what the optimal value of h-index is
		# So we can straight away return that value
        if n - mid == citations[mid]: return citations[mid]
            
		# If there are more than h papers with citations >= h 
		# This is a valid h-index. But we want to maximize this value
		# Hence we keep searching on right side of mid
        if n - mid > citations[mid]: start = mid + 1
			
		# But if there are less than "h" papers with citations >= h
		# That means, the current "h-index" value cannot be valid
		# And since array is sorted, no value after it can be valid as well
		# Hence, we will search for a valid h-index value on left side of mid
        else: end = mid - 1
        
	# Finally, ( length of the array - start index) is the required h-index value
    return n - start


citations = [0,1,3,5,6]
print("H-index is -> ", hIndex(citations))