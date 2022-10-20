def triangleNumber(nums):
        count = 0
        
        # Sort the list in increasing order
        nums.sort()
        
        n = len(nums)
        
        
        # Initially, "c" points to the largest value in the list i.e., last index
        # a points to the smallest value in the list i.e., first index
        # b points to the value just before "c" i.e., last index - 1
        i = n - 1
        while i >= 2:
            # a => first side
            # b => second side
            # c => third side (largest of two)
            a,b,c = 0, i - 1, i
            
            
            while a < b: 
                side1,side2,side3 = nums[a], nums[b], nums[c]
                
                # If this is true for any "a" and "b"
                # Then this will be true for any value between "a" and "b" as well
                # Because list is sorted
                if side1 + side2 > side3:
                    # Hence, increment count by number of values between "b" and "a" indices (both included)
                    count += b - a
                    # Decrement "b" pointer
                    b -= 1
                else:
                    # Otherwise, increment "a" pointer
                    a += 1
            
            # After each iteration, decrement the "c" pointer
            i -= 1
                    
        return count

nums = [2,2,3,4]

print("Number of valid triplets -> ", triangleNumber(nums))