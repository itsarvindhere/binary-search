from collections import defaultdict
from math import ceil
from sortedcontainers import SortedList
class TweetCounts:
    
    # Using a SortedList instead of a normal list
    # We can ensure that time values for the tweet is in a sorted order as we insert them
    def __init__(self):
        self.dict = defaultdict(SortedList)
        
    # In a SortedList, addition is an almost O(LogN) operation
    # As we insert any value, it is automatically put at its correct place to maintain the sorted order
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.dict[tweetName].add(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int):
        output = []
        
        # How many chunks will be there
        # For ex. if freq is "minutes" there will be chunks of 60 seconds.
        # So lets find how many chunks will be there based on "freq" that we get
        
        # We also keep a variable that stores the value which is the size of each chunk
        count = 0
        size = 0
        
        if freq == "minute": 
            count = ceil((endTime - startTime + 1) / 60)
            size = 60
        elif freq == "hour": 
            count = ceil((endTime - startTime + 1) / 3600)
            size = 3600
        else: 
            count = ceil((endTime - startTime + 1) / 86400)
            size = 86400

            
        # Now for each chunk, we need to find how many tweets are there
        freqList = self.dict[tweetName]
        
        prevEndTime = 0
        
        for i in range(count):
            
            # First, get the start and end time of this chunk
            chunkStartTime = startTime if prevEndTime == 0 else prevEndTime + 1
            chunkEndTime = chunkStartTime + size - 1
            
            if chunkEndTime > endTime: chunkEndTime = endTime
            
            # Since list is sorted, we can use Binary Search
            # We first find the index of leftmost time value which is >= chunkStartTime
            start = 0
            end = len(freqList) - 1
            leftmostIndex = -1
            
            while start <= end:
                mid = start + (end - start) // 2
                if freqList[mid] >= chunkStartTime:
                    leftmostIndex = mid
                    end = mid - 1
                else: start = mid + 1
            
            # If we couldn't find any index then stop. We are done with this chunk
            if leftmostIndex == -1: 
                output.append(0)
                continue
            
            # We then find the index of rightmost time value which is <= chunkEndTime
            start = 0
            end = len(freqList) - 1
            rightmostIndex = -1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                if freqList[mid] <= chunkEndTime:
                    rightmostIndex = mid
                    start = mid + 1
                else: end = mid - 1
            
            output.append(rightmostIndex - leftmostIndex + 1)
            
            # Set the previous end time as the current chunk's end time
            # So that in next iteration, we can use this previous end time to start a new chunk
            prevEndTime = chunkEndTime
            
        
        return output