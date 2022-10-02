def findKthPositive(arr, k):
    # Since the array is already sorted, why not use Binary Search
    # Because we can get a solution in O(logN) time using Binary Search
                
    start = 0
    end = len(arr) - 1
        
    while start <= end:
        mid = start + (end - start) // 2
        
        # How many elements are missing till mid?
        # Ideally, mid should have element = mid + 1
        # If element at mid is not mid + 1, that means there are some missing numbers before mid
        # And Count of missing numbers till mid = (current element at mid - correct element at mid)

        # If count of missing till mid is < k 
        # That means we need to look at right side of mid for kth missing
        if arr[mid] - (mid + 1) < k: start = mid + 1
        # Otherwise, look at the left side of mid
        else: end = mid - 1
        
        
    # At this point, the end pointer will point to index of largest element that is smaller than kth missing
    # So kth missing = end + k + 1
    return end + k + 1


arr = [2,3,4,7,11]
k = 5

print("Kth Missing Positive Number is -> ", findKthPositive(arr,k))