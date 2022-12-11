# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Let us first try to find the peak index in the mountain_arr
        n = mountain_arr.length()
        
        start = 0
        end = n - 1
        peakIndex = 0
        
        while start <= end:
            mid = start + (end - start) // 2
            
            elementBeforeMid = -1 if mid == 0 else mountain_arr.get(mid - 1)
            elementAtMid = mountain_arr.get(mid)
            elementAfterMid = -1 if mid == n - 1 else mountain_arr.get(mid + 1)
            
            # If mid is the peak 
            if elementAtMid >= elementBeforeMid and elementAtMid >= elementAfterMid:
                peakIndex = mid
                break
                
            # If mid is not peak, move toward where we can find the peak index
            if elementBeforeMid > elementAtMid and elementAfterMid > elementAtMid:
                if elementBeforeMid > elementAfterMid:
                    end = mid - 1
                else: start = mid + 1
                    
            elif elementBeforeMid > elementAtMid:
                end = mid - 1
            else: start = mid + 1
                
                
        # Now that we got the peak index, we can now binary search on [start, peakIndex] and [peakIndex, end]
        # [start, peakIndex] is in increasing order and  [peakIndex, end] is in decreasing order
        
        # Index to return
        minIndex = -1
        
        # First, let us binary search on the [start, peakIndex]
        start = 0
        end = peakIndex
        
        while start <= end:
            mid = start + (end - start) // 2
            
            elementAtMid = mountain_arr.get(mid)
            
            # If at mid, we have the target, this may be the minumum index
            # But to be sure, we want to keep searching on left side of mid
            if elementAtMid == target:
                minIndex = mid
                end = mid - 1
            elif elementAtMid < target: 
                start = mid + 1
            else: 
                end = mid - 1
        
        
        # If we get a minIndex here itself, no need to binary search in [peakIndex, end]
        # Because we cannot get a minimum index than current minimum in [peakIndex, end]
        if minIndex != -1: return minIndex
        
        # Otherwise, we can Binary Search on [peakIndex, end]
        # First, let us binary search on the [start, peakIndex]
        start = peakIndex
        end = n - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            elementAtMid = mountain_arr.get(mid)
            
            # If at mid, we have the target, this may be the minumum index
            # But to be sure, we want to keep searching on left side of mid
            # Do note that we want the "minimum" index
            # So even if array is in decreasing order, we will still search on left side for minimum index
            if elementAtMid == target:
                minIndex = mid
                end = mid - 1
            elif elementAtMid < target: 
                end = mid - 1
            else: 
                start = mid + 1

        return minIndex