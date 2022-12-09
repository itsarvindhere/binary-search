class Solution: 
    # Helper method to find how many pairs have distance <= X
    def isValid(self, nums, x, k):
        count = 0
        
        n = len(nums)

        # To keep track of the rightmost valid index for the previous element
        # Because for the new element, all the elements till "rightmost" index will be valid too
        prevIndex = 1
        
        # For each element
        for i in range(n):
            
            # Binary search for the rightmost element that will give distance of <= x
            # Then, all elements in between, will have distance <= x when paired with "ith" element
            start = prevIndex
            end = n - 1
            rightmostIndex = -1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                distance = abs(nums[i] - nums[mid])
                
                if distance <= x:
                    rightmostIndex = mid
                    # Update the previous index so that 
                    # we search after this "rightmostIndex" for the next element
                    prevIndex = mid
                    start = mid + 1
                else: end = mid - 1
            
            
            count += 0 if rightmostIndex < 0 else rightmostIndex - i
            
            if count >= k: return True
            
        return False
            
    
    def smallestDistancePair(self, nums, k):
        
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