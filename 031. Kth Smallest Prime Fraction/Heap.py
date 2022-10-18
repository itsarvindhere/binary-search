from heapq import heappop, heappush
def kthSmallestPrimeFraction(arr, k):
    # Kth Smallest means we need a maxHeap such that we discard all the bigger fractions from top
    # We will maintain the size of heap as K
        
    heap = []
        
    # For each element in the array
    for i in range(len(arr)):
        # Go through each element after it
        for j in range(i+1, len(arr)):
            # Calculate the fraction
            fraction = arr[i]/arr[j]
                
            # Push the fraction into the heap, along with the ith and jth values
            heappush(heap, (-fraction, arr[i], arr[j]))
                
            # If the heap size becomes more than k, pop the topmost element
            if len(heap) > k: heappop(heap)
                
    # At the end, the top of heap will have the kth smallest fraction
    return [heap[0][1], heap[0][2]]

arr = [1,2,3,5]
k = 3

print("Kth Smallest Fraction -> ", kthSmallestPrimeFraction(arr, k))