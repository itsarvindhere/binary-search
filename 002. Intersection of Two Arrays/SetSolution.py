# Using extra space - O(n) Time and O(n) Space
def intersection(nums1, nums2):
        
    #List to return
    output = set()
        
    # Create a set of the first list so that only uniques are present
    setOfList1 = set(nums1)
        
    # Now check what numbers from list2 are present in the set above
    # Add those numbers in output list
    # As we know, for a set, searching is a constant time operation
    for num in nums2: 
        if num in setOfList1: output.add(num)

    return list(output)
        

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print("Intersection array ->", intersection(nums1, nums2))