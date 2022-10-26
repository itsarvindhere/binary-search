def checkIfExist(arr):
        # To apply Binary Search, first sort the list
        arr.sort()
        
        n = len(arr)
        
        # For each element in the list
        for i,num in enumerate(arr):
            # Binary Search for its double
            start, end = 0, n - 1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                # We also need to make sure i != j
                if arr[mid] == 2 * num and i != mid: return True
                
                # If the element at mid is less than the double of num
                # Then search for double at right of mid
                if arr[mid] < 2 * num: start = mid + 1
                    
                # Otherwise search for the double at the left side of mid
                else: end = mid - 1
                    
        
        return False


arr = [10,2,5,3]

print(checkIfExist(arr))