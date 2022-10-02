from collections import Counter
def intersect(nums1, nums2):
    # Output that we want to return
    output = []
            
    # To keep the count of each element in nums2
    count = Counter(nums2)
            
    # Now for each element in first array
    for num in nums1:
        # If count of that element is > 0 we can include it
        if num in count and count[num] > 0:
            output.append(num)
            # Reduce its count by 1 as we included this element once in the output
            count[num] -= 1
     
    return output


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print("Intersection Array is -> ", intersect(nums1,nums2))