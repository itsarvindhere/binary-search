def maxDistance(nums1, nums2) -> int:
    # Since both arrays are sorted in non-decreasing order
    # We can try two pointer approach here
    
    i = 0
    j = 0
    maxDistance = 0
    
    while i < len(nums1) and j < len(nums2):   
        # If nums2[j] >= nums1[i] that means it is one possible solution
        # But because we want to maximize the distance, we increment j
        # Because if next element also satisfies this condition, then it will have a larger distance
        if nums2[j] >= nums1[i]: 
            maxDistance = max(maxDistance, j - i)
            j += 1
        
        else: 
            i += 1
            # We also want to make sure i is <= j
            if i > j: j += 1
            
    return maxDistance


nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]

print("Maximum Distance of any valid pair is -> ", maxDistance(nums1,nums2))