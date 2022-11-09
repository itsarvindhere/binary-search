from collections import defaultdict
class RangeFreqQuery:

    def __init__(self, arr):
        # For every element, keep a list of indices at which it is present in the array
        self.dict = defaultdict(list) 
        for i,num in enumerate(arr): self.dict[num].append(i)
        

    def query(self, left: int, right: int, value: int) -> int:
        
        # The list in which we have to count the occurances of 'value'
        indices = self.dict[value]
        
        # Now, first, we will find the smallest index that is >= left
        start = 0
        end = len(indices) - 1
        leftmostIndex = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if indices[mid] >= left:
                leftmostIndex = mid
                end = mid - 1
            else: start = mid + 1
        
        # If leftmost index is -1, that means this subarray does not have a single "value"
        if leftmostIndex == -1: return 0
        
        # Next, we will find the largest index that is <= right
        start = 0
        end = len(indices) - 1
        rightmostIndex = -1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if indices[mid] <= right:
                rightmostIndex = mid
                start = mid + 1
            else: end = mid - 1
                
        # And once we get the two indices, just return how many times "value" occurs between these indices
        # That is, (leftindex - rightindex + 1)
        return rightmostIndex - leftmostIndex + 1


rangeFreqQuery = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);

print(rangeFreqQuery.query(1,2,4))
print(rangeFreqQuery.query(0,11,33))