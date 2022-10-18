class TopVotedCandidate:

    def __init__(self, persons, times):
        # We will keep the track of who was leading at ith time in this list
        self.leadingCount = []
        
        # We will use this to keep track of the votes casted to each person
        count = {}

        # This will be used to keep track of most votes casted to any person so far
        mostVotes = 0

        # This is used to keep track of the leading person
        leadingPerson = -1
        
        
        for i,person in enumerate(persons):
            count[person] = count.get(person, 0) + 1
            
            # Since we are asked to choose the most recently votes candidate in case of a tie
            # We also need to cover the "equals to" part here, not just "greater than"
            if count[person] >= mostVotes:
                mostVotes = count[person]
                leadingPerson = person
                
            # Which person was leading at ith time? Add that data to the list
            self.leadingCount.append((times[i], leadingPerson))
            

    def q(self, t: int) -> int:
        
        # Since the leadingCount is already in sorted order based on the time, apply Binary Search
        start = 0
        end = len(self.leadingCount) - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            # If "mid" time is the same as "t", return the person who was leading at this time
            if self.leadingCount[mid][0] == t: return self.leadingCount[mid][1]
            
            # If "mid" time is greater than "t" then search on left side of "mid"
            if self.leadingCount[mid][0] > t: end = mid - 1
            
            # If "mid" time is less than "t" then search on right side of "mid"
            else: start = mid + 1
            
        # In the end, if "t" time is not at all there in the list, "end" will point to the 
        # largest time value that is smaller than "t" i.e., floor of "t"
        return self.leadingCount[end][1]


persons = [0, 1, 1, 0, 0, 1, 0]
times = [0, 5, 10, 15, 20, 25, 30]
obj = TopVotedCandidate(persons, times)

print("Person leading at time 24 -> ", obj.q(25))
