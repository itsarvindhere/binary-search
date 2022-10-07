def maximumGroups(grades):
    
    # Output to return
    count = 0
        
    n = len(grades)
        
    # The valid range of number of groups is 1 to n
    for i in range(1, n + 1):
        # For each i, try to check if we can have "i" groups for n grades
        if i * (i + 1) / 2 <= n: count = i
        # If i is not valid, no need to check for values greater than i as they'll be invalid too
        else: break

    return count
                

grades = [10,6,12,7,3,5]
print("Maximum Number of Groups -> ", maximumGroups(grades))