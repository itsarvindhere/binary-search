class Solution: 
    # Helper method to find how many pairs have distance <= X
    def isValid(self, nums, x, k):
        count = 0
        
        n = len(nums)
        
        # Since array is sorted, it means, if for an element "i", we get the rightmost index as "j"
        # Then for any element between "i" and "j" as well, the count of pairs with distance <= x will be at least ( j - i)
        # It means, we can use sliding window approach here
        i,j = 0,0
        
        while j < n:
            
            # While our window is not valid, shrink it
            while (nums[j] - nums[i]) > x: i += 1

            # When we are here, we know that this whole window is valid
            # So, there are "j - i" pairs in this window that have distance <= x
            count += j - i
            
            # Increase window size from right
            j += 1

        return count >= k
            
    
    def smallestDistancePair(self, nums, k) -> int:
        
        # Sorted nums for the helper method
        nums.sort()
        
        # Can we try to Binary Search the Answer?
        
        # We want to find the "kth" smallest distance
        # So, what can be the "smallest" distance?
        # Since nums[i] can be 0, smallest distance can be 0 as well.
        
        start = 0
        
        # And what can be the "max" distance?
        # It can be 10^6. Suppose if we have "0" and "10^6" in an array
        # Even more simpler, it can be the maximum value in given array
        
        end = nums[-1]
        
        # And now, in this range, there is certain distance value that is the kth smallest distance
        # So, at every "mid" we will get a "distance value". And we have to find how many pairs have distance <= mid
        # If we have ">= k" pairs that have distance <= mid, we know that kth smallest is either "mid" or is present on the left of "mid"
        # Otherwise, it will be on right of mid
        
        kthSmallestDistance = 0

        while start <= end:
            mid = start + (end - start) // 2
            
            # "mid" distance will be valid if there are k or more pairs with distance <= "mid"
            # In that case, "mid" may be the kth smallest but to be sure, we will keep searching on left side of mid
            if self.isValid(nums,mid,k): 
                kthSmallestDistance = mid
                end = mid - 1
            # Otherwise, kth smallest distance is on right side
            else: start = mid + 1
        
        # Finally, after we come out of the while loop, return the kth smallest distance
        return kthSmallestDistance


solution = Solution()

nums = [1,5,10,6,7,2,1,1,0,2]
k = 6

print("Kth Smallest Pair -> ", solution.smallestDistancePair(nums, k))