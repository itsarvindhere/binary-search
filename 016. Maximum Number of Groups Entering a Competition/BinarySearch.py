def maximumGroups(grades):
        
    # Output to return
    count = 0
        
    # Binary Search on Answer
    n = len(grades)

    start = 1
    end = n
        
    while start <= end:
        mid = start + (end - start) // 2
        # Check if there can be 'mid' groups for 'n' grades
        # If there can be 'mid' groups, keep checking on right side of mid for a bigger valid value
        if mid * (mid + 1) / 2  <= n:
            count = mid
            start = mid + 1
        # If there cannot be 'mid' number of groups, all numbers greater than mid are also invalid
        else:
            end = mid - 1

    return count


grades = [10,6,12,7,3,5]
print("Maximum Number of Groups -> ", maximumGroups(grades))