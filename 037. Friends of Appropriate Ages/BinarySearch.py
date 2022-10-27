def numFriendRequests(ages):
        requestCount = 0
        
        # Sort the list before applying Binary Search on it
        ages.sort()
        
        n = len(ages)
        
        for i in range(n):

            # First, find the index of smallest possible value of "y"
            # That is, the smallest value in the array that is > 0.5 * age[x] + 7
            
            leftmostValidIndex = -1
            
            start, end = 0, n - 1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                if ages[mid] > 0.5 * ages[i] + 7:
                    leftmostValidIndex = mid
                    end = mid - 1
                else: start = mid + 1
                    
            # If we couldn't find any valid value that is > 0.5 * age[x] + 7
            if leftmostValidIndex < 0: continue
                    
            # Now, find the index of largest possible value of "y"
            # That is, the largest value in the array that is <= x
            
            rightmostValidIndex = -1
            start, end = 0, n - 1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                if ages[mid] <= ages[i]:
                    rightmostValidIndex = mid
                    start = mid + 1
                else: end = mid - 1
                    
            # How many ages are there to which we can send friend request?
            count = rightmostValidIndex - leftmostValidIndex
            requestCount += count if count > 0 else 0
            
        
        return requestCount


ages = [20,30,100,110,120]
print("Total Number of Friend Requests -> ", numFriendRequests(ages))