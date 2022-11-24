def minAbsoluteSumDiff(nums1, nums2): 
    absSumDiff = 0
        
    # This will be used to keep track of maximum possible reduction in the absolute difference after replacing an element
    # That is, max value of (Initial abs difference of that element - abs difference after replacing that element)
    maxAbsDiffVal = 0
        
    mod = (10 ** 9) + 7

    sortedNums1 = sorted(nums1)
    n = len(nums1)
        
    # For each value in nums2
    for i in range(n):
            
        # We will get the absolute difference (without taking into account any replacements)
        diff = abs(nums1[i] - nums2[i])
            
        # This is to track the absolute sum difference without any replacements
        absSumDiff += diff
            
        # Now, for this nums[i], what is other number that we can replace it with
        # Such that, "diff" can be reduced to minimum possible value?
        # We will use Binary Search here
        # Because, for minimum possible abs difference, we need the floor and ceil values for nums2[i] in sortedNums1
        # One of those two will give us the minimum possible difference (both can also give us min difference)
            
        # Floor means the largest value that is <= nums2[i] 
        # Ceil means the smallest value that is >= nums2[i]
            
        # Simply put, the closest number to nums2[i] in the sortedNums1 will give us minimum difference
        # And closest number if either the floor value or ceil value
            
        start = 0
        end = n - 1
            
        floor = -1
        ceil = -1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            # If we have nums2[i] in sortedNums1, then that will give us the minimum possible abs difference value, that is, 0
            # So there can be no other value that gives us a lower possible difference since all are positive numbers only
            # Hence we can break if this is the case
            if sortedNums1[mid] == nums2[i]:
                floor = sortedNums1[mid]
                ceil = sortedNums1[mid]
                break
                
            if sortedNums1[mid] < nums2[i]:
                floor = sortedNums1[mid]
                start = mid + 1
            else:
                ceil = sortedNums1[mid]
                end = mid - 1
            
        # If the number is the first number in the sorted list, ofcourse there cannot be a floor value
        # In that case, we simply consider the ceil only
        if floor == -1:
            maxAbsDiffVal = max(maxAbsDiffVal, diff - abs(ceil - nums2[i]))
        # If the number is the last number in the sorted list, ofcourse there cannot be a ceil value
        # In that case, we simply consider the floor only
        elif ceil == -1:
            maxAbsDiffVal = max(maxAbsDiffVal, diff - abs(floor - nums2[i]))
        else:
            diff1 = max(maxAbsDiffVal, diff - abs(floor - nums2[i]))
            diff2 = max(maxAbsDiffVal, diff - abs(ceil - nums2[i]))
                
            maxAbsDiffVal = max(diff1, diff2)
        
    # At the end, maxAbsDiffVal will be the maximum possible value by which we can reduce "absSumDiff" by replacing one element in nums1
    return (absSumDiff - maxAbsDiffVal) % mod


nums1 = [1,10,4,4,2,7]
nums2 = [9,3,5,1,7,4]

print("Minimum Absolute Sum Difference -> ", minAbsoluteSumDiff(nums1, nums2))

