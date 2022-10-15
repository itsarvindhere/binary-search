def maxDistance(nums1, nums2):
    # Because we are given that both arrays are sorted in decreasing order
    # We can use Binary search instead of linear search in the inner loop
    
    maxDistanceSoFar = 0
    
    for i,num1 in enumerate(nums1):
        # Binary search for the maximum index on right of i index at which element is >= num1
        start = i
        end = len(nums2) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            # If mid element is greater than num1, that's one possible solution
            # But we want to maximize the distance
            if nums2[mid] >= num1:
                maxDistanceSoFar = max(maxDistanceSoFar, mid - i)
                start = mid + 1
            else: end = mid - 1
                
    return maxDistanceSoFar


nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]

print("Maximum Distance of any valid pair is -> ", maxDistance(nums1,nums2))