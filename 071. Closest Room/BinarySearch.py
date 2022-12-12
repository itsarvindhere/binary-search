from sortedcontainers import SortedList 
class Solution:
    def closestRoom(self, rooms, queries):
        
        k = len(queries)

        answer = [-1] * k
        
        # Sort the rooms based on their size in Decreasing order
        rooms.sort(key = lambda x: x[1], reverse=True)
        
        # Sort the Queries by the minSize but in decreasing order
        # Because if for the query with biggest minSize value, we can create a Sortedlist of valid rooms
        # That list can then be used for every query that has a smaller of equal minSize
        
        # Also, since the "answer" has elements in same order as queries originally
        # WE do not want to lose track of original indices
        queries = [(query[1], query[0], i) for i,query in enumerate(queries)]
        
        # Now sort based on the MinSize in Decreasing order
        queries.sort(reverse=True)
        
        # List of valid rooms that can be the candidates
        candidates = SortedList()
        
        j = 0
        
        # For each query
        for minSize, preferred, i in queries:
            # Create the candidate list
            while j < len(rooms) and rooms[j][1] >= minSize:
                candidates.add(rooms[j][0])
                j += 1
                
            # Now, among these candidate rooms, we will search for the id that is closest to "preferred"
            # The id closest to "preferred" will be either floor or ceil of "preferred" in the candidates list
            # for that, we will use binary search
            
            # First, let's find the floor
            # That is, the biggest id that is <= "preferred"
            start = 0
            end = len(candidates) - 1
            floorIdx = -1
            
            while start <= end:
                mid = start + (end - start) // 2
            
                if candidates[mid] <= preferred:
                    floorIdx = mid
                    start = mid + 1
                else: end = mid - 1
                    
            # Next, let's find the ceil
            # That is, the smallest id that is >= "preferred"
            start = 0
            end = len(candidates) - 1
            ceilIdx = -1
            
            while start <= end:
                mid = start + (end - start) // 2
            
                if candidates[mid] >= preferred:
                    ceilIdx = mid
                    end = mid - 1
                else: start = mid + 1
            
            # If both are -1, then there is no valid room available
            if floorIdx == -1 and ceilIdx == -1: answer[i] = -1
            else: 
                diff1 = abs(candidates[floorIdx] - preferred)
                diff2 = abs(candidates[ceilIdx] - preferred)
                
                answer[i] = candidates[floorIdx] if diff1 <= diff2 else candidates[ceilIdx]     
        
        return answer


solution = Solution()

rooms = [[2,2],[1,2],[3,2]]
queries = [[3,1],[3,3],[5,2]]

print("Output -> ", solution.closestRoom(rooms, queries))