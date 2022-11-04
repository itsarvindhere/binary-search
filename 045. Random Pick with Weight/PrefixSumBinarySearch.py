import random
class Solution:

    def __init__(self, w):   
        # Convert the list into a prefix sum array
        for i in range(1, len(w)): w[i] += w[i - 1]
        
        self.w = w


    def pickIndex(self) -> int:
        
        # The random number should be anything from 1 to sum of w
        # Since that's the range of values
        target = random.randint(1, self.w[-1])
        
        # Now we want the closest element to this target
        start = 0
        end = len(self.w) - 1
        index = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if self.w[mid] == target:  return mid
            
            if self.w[mid] < target:
                start = mid + 1
            else: end = mid - 1
        
        return start