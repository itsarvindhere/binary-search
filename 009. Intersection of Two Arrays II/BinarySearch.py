def intersect(nums1, nums2):
    # Output that we want to return
    output = []
            
    # To keep the count of each element of nums2
    count = [0] * 1001
    for num in nums2: count[num] += 1
            
    # Sort the second array
    nums2.sort()
                
    # For each element in first array
    for num1 in nums1:
        # Binary Search the second array
        start = 0
        end = len(nums2) - 1
                
        while start <= end:
            mid = start + (end - start) // 2
            if nums2[mid] == num1 and count[num1] > 0:
                output.append(num1)
                count[num1] -= 1
                break
            if nums2[mid] < num1: start = mid + 1
            else: end = mid - 1

    return output


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print("Intersection Array is -> ", intersect(nums1,nums2))