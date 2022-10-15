def maxDistance(nums1, nums2):
    # In Brute force approach, for each element in nums2
    # we go through each less or equal element in nums2
    # And we keep track of the maximum distance
        
    maxDistanceSoFar = 0
        
    for i,num1 in enumerate(nums1):
        for j in range(i, len(nums2)):
            if num1 <= nums2[j]: maxDistanceSoFar = max(maxDistanceSoFar, j - i) 
            else: break
        
    return maxDistanceSoFar


nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]

print("Maximum Distance of any valid pair is -> ", maxDistance(nums1,nums2))