#Using Binary Search  - O(nlogn) Time and O(1) Space
def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
        
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target: return True
        elif arr[mid] > target: end = mid - 1
        else: start = mid + 1
        
        
    return False
    
    
def intersection(nums1, nums2):
    nums2.sort()
        
    output = set()
        
    for num in nums1:
        if binarySearch(nums2, num): output.add(num)

    return list(output)


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print("Intersection array ->", intersection(nums1, nums2))