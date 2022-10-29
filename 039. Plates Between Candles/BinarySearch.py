def platesBetweenCandles(s,queries):
        # Output array to return
        output = []
        
        # Array of indices of all the candles in the given string
        candleIndices = []
        
        # Precompute how many plates are there till any index
        plates = []

        for i in range(len(s)):
            prevPlates = 0 if i == 0 else plates[i-1]
            
            if s[i] == "*": plates.append(prevPlates + 1)
            else: 
                candleIndices.append(i)
                plates.append(prevPlates)
        
        # Now, for every query, we first find the leftmost candle and rightmost candle
        # Because we have to only find plates "between" candles
        # This means, every valid plate will have at least one candle to its left and to its right side
        
        for left, right in queries:
            
            # if left and right indices are the same
            if left == right: 
                output.append(0)
                continue
            
            # Binary Search for the index of leftmost candle
            start = 0
            end = len(candleIndices) - 1
            
            leftmostIndex = -1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                if candleIndices[mid] < left:
                    start = mid + 1
                else:
                    leftmostIndex = candleIndices[mid]
                    end = mid - 1
                    
            # If leftmost index not found that basically means there is no candle in this substring
            if leftmostIndex == -1: 
                output.append(0)
                continue
            
            # Binary Search for the index of rightmost candle
            start = 0
            end = len(candleIndices) - 1
            
            rightmostIndex = -1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                if candleIndices[mid] > right:
                    end = mid - 1
                else:
                    rightmostIndex = candleIndices[mid]
                    start = mid + 1
                    
            count = 0
            
            # If the rightmost index  is not found or leftmostIndex is greater than rightmostIndex
            # In both cases, there are no plates between the candles in this substring
            # So, except those cases, we want to find number of plates between these two indices
            if not (rightmostIndex == -1 or leftmostIndex >= rightmostIndex):
                # Now we want the number of plates between these two indices
                count = plates[rightmostIndex] - plates[leftmostIndex]

            output.append(count)
        
        return output

s = "***|**|*****|**||**|*"
queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]

print("Output -> ", platesBetweenCandles(s, queries))

