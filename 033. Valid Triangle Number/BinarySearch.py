def triangleNumber(nums):
        count = 0
        
        # Sort the list in increasing order
        nums.sort()
        
        n = len(nums)
        
        for i in range(n - 2):
            k = i + 2
            if nums[i] != 0:
                for j in range(i + 1, n - 1):

                    # Binary Search for the third side
                    start = k
                    end = n - 1
                    res = None

                    while start <= end:
                        mid = start + (end - start) // 2

                        if nums[i] + nums[j] > nums[mid]:
                            res = mid
                            start = mid + 1
                        else: end = mid - 1

                    if res: 
                        k = res
                        count += res - j
                
        return count

nums = [2,2,3,4]

print("Number of valid triplets -> ", triangleNumber(nums))