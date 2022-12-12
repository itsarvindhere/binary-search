# PROBLEM STATEMENT

There is a hotel with n rooms. The rooms are represented by a 2D integer array rooms where rooms[i] = [roomIdi, sizei] denotes that there is a room with room number roomIdi and size equal to sizei. Each roomIdi is guaranteed to be unique.

You are also given k queries in a 2D array queries where queries[j] = [preferredj, minSizej]. The answer to the jth query is the room number id of a room such that:

    1. The room has a size of at least minSizej, and
    2. abs(id - preferredj) is minimized, where abs(x) is the absolute value of x.
    3. 
If there is a tie in the absolute difference, then use the room with the smallest such id. If there is no such room, the answer is -1.

Return an array answer of length k where answer[j] contains the answer to the jth query.

# EXAMPLE

    Input: rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
    Output: [3,-1,3]

Explanation: The answers to the queries are as follows:
Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.


# BINARY SEARCH APPROACH

Why are we sorting the Queries based on the "MinSize" in Decreasing order? 

Because if you think, if for the query with the biggest value of "minSize", we can create a list of candidate rooms, then that list will be valid for every other query. We may add some more rooms in that for other queries, but the list for previous query will be valid for next one as well.

And only from that list itself, we will get any valid roomId for any query. So, the main thing is to construct this list of candidate rooms from which we have to find the one we are looking for.

Let's understand it with an example. 

		rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]]
		queries = [[2,3],[2,4],[2,5]]
		
		We will sort "queries" in decreasing order based on "minSize"
		And since the final output list is constructed based on the queries, we also keep the original indices
		
		So, we convert each query to a tuple (minSize, preferred, index)
		
		And then we sort in decreasing order. So now, queries become - 
		
		queries = [(5,2,2), (4,2,1), (3,2,0)]
		
		Now, we can create a candidate list where we keep all those rooms that may be the solutions for this query.
		
		Suppose, we have the first query (5,2,2)
		
		Then here, we have minSize = 5, preferred = 2 and index = 2
		
		So, all those rooms for which size >= 5 are all valid solutions for this query.
		
		And we only have one room that satisfies this condition -> [[3,5]]
		
		Now, to quickly create candidate list, we can sort the rooms in decreasing order based on size as well.
		
		So that as soon as we get to a room that is not valid, we know all rooms after it are not valid as well so we stop.
		
		And once we have the candidates, all we are looking for is the room with the roomId that is closest to "preferred"
		
		
Because, abs(id - preferred) will be minimized if "id" is closest to "preferred" value. And that means, we need to Binary search for the "floor" and "ceil" value of "preferred" in candidates list. Because either floor or ceil or both are closest to "preferred". In case of a tie, we can choose the "floor" value.

 