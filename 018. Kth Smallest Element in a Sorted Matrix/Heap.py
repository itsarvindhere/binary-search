from heapq import heappush, heappop
def kthSmallest(matrix, k):
    heap = []
        
    n = len(matrix)
        
    # We can use a MaxHeap and keep pushing elements in it
    # Since it is a MaxHeap, all the bigger elements are on top
    # And we also make sure the size of heap does not exceed k
    for row in range(n):
        for col in range(n):
            heappush(heap, -matrix[row][col])
            if len(heap) > k: heappop(heap)
                    
    # Finally, the top element will be the kth smallest element in this matrix
    return -heap[0]


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print("Kth smallest element is -> ",kthSmallest(matrix, k))