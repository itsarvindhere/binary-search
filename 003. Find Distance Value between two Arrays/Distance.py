def findTheDistanceValue(arr1, arr2, d):
    count = 0
        
    # Sort the Second array to apply binary search on it
    arr2.sort()
        
    # For Each Number in first list, check if the second list contains any invalid element
    # An element arr2[i] is invalid if abs(arr1[i] - arr2[i]) <= d
    # If invalid, reduce the count
    for num in arr1: 
        # Binary Search Instead of linear search
        start,end = 0, len(arr2) - 1
        isValid = True
        while start <= end:
            mid = start + (end - start) // 2
            # If any invalid value found, break
            if abs(num - arr2[mid]) <= d:
                isValid = False
                break
            #If mid is valid and less than the number
			# That means any value less than mid is also valid as array is sorted
			# So there is no need to look at left of mid at all as all values are valid
            if arr2[mid] < num: start = mid + 1
            else: end = mid - 1
        if isValid: count += 1

    return count

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2


print("Count of Valid Values -> ", findTheDistanceValue(arr1,arr2,d))