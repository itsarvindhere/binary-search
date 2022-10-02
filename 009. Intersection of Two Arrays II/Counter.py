def intersect(nums1, nums2):
    # Output that we want to return
    output = []
            
    # Sort Both lists
    nums1.sort()
    nums2.sort()
            
    # Now for each element in first array
    i,j = 0,0
            
    # Since both are sorted, we can start from beginning of both lists
    while i < len(nums1) and j < len(nums2):
        # If ith element of nums1 is smaller than jth element of num2
        # Then we need to increment i because we are looking for same elements
        if nums1[i] < nums2[j]: i += 1
        # If ith element of nums1 is larger than jth element of num2
        # Then we need to increment j because we are looking for same elements
        elif nums1[i] > nums2[j] : j += 1
        # Otherwise, we found two same elements so we can append that element in output list
        else:
            output.append(nums1[i])
            # And also incremebt both indices because we are done with ith and jth elements
            i += 1
            j += 1
            
    return output


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print("Intersection Array is -> ", intersect(nums1,nums2))