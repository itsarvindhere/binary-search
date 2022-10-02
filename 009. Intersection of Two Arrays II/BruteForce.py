def intersect(nums1, nums2):
        # Output that we want to return
        output = []
            
        # To keep the count of each element of nums2
        count = [0] * 1001
        for num in nums2: count[num] += 1
                
        # For each element in first array
        for num1 in nums1:
            # Go through each element in second array
            for num2 in nums2:
                # If both numbers are same and count is more than 0
                if (num1 == num2) and (count[num2] > 0):
                    # Append the number to the output list
                    output.append(num1)
                    # Also, decrement its count
                    count[num2] -=1
                    # Break out of this inner loop as we found the matching element for num1
                    break
        return output


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print("Intersection Array is -> ", intersect(nums1,nums2))