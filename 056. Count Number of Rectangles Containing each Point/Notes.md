# PROBLEM STATEMENT

You are given a 2D integer array rectangles where rectangles[i] = [li, hi] indicates that ith rectangle has a length of li and a height of hi. You are also given a 2D integer array points where points[j] = [xj, yj] is a point with coordinates (xj, yj).

The ith rectangle has its bottom-left corner point at the coordinates (0, 0) and its top-right corner point at (li, hi).

Return an integer array count of length points.length where count[j] is the number of rectangles that contain the jth point.

The ith rectangle contains the jth point if 0 <= xj <= li and 0 <= yj <= hi. Note that points that lie on the edges of a rectangle are also considered to be contained by that rectangle.

# EXAMPLE

    Input: rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
    Output: [2,1]

Explanation: 

The first rectangle contains no points.
The second rectangle contains only the point (2, 1).
The third rectangle contains the points (2, 1) and (1, 4).
The number of rectangles that contain the point (2, 1) is 2.
The number of rectangles that contain the point (1, 4) is 1.
Therefore, we return [2, 1].

# **1. BRUTE FORCE APPROACH - TLE**
A Brute force approach is never going to work as the constraints say the length of the lists can be up to 5 * 10^4!

But, from here, we can start thinking of how we can optimize this solution such that it is accepted.

# **2. BINARY SEARCH APPROACH**

We see that the main reason why the Brute Force approach is failing for large inputs is because for every point, we have to traverse the rectangles list from beginning to end. But if you take a look at the constraints carefully, while the lengths can be up to  10^9, the heights can be up to 100 only. And this constraint is given for a reason. Because we have to map the lengths based on the heights.

See, since height can be from 1 to 100, we know that for any point, any rectangle that contains that point should have height >= point[1]. For if we already know that for heights >= point[1], how many rectangles are there and what are their lengths, then all that is left to find is how many rectangles have length >= point[0]. And to optimize that, we can use Binary Search if the rectangles list is alrady sorted based on the lengths. Because in that case, we know that if one rectangle contains a point, all rectangles after it contain it as well. So all that we want is the leftmost rectangle that contains a particular point.

	Take this example - rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]
	
	The list is already in sorted order. 
	
	We will create a map where key is the height and value is a list 
	containing the lengths of rectangles with that height.
	
	Hence, for above list, our map is like - 
	
	dict = { 2: [1], 3: [2, 3, 6], 5: [2]}
	
	It means, for height = 3, we have 3 rectangles with lengths 2, 3 and 6.
	

Now, for each point, all we want to do is traverse over all the lists of heights where height >= point[1].

	First point is [1,3]. It means, "y" value is 3. 
	
	So any rectangle with height >= 3 should be a candidate. 
	
	Hence, we traverse from heights 3 to 100 (since 100 is the upper limit)
	
	And for each height in the map, for its corresponding list, we can use Binary Search.
	
We Binary search for the leftmost length such that length >= point[0]
	
And once we get the leftmost index, we increment count by len(dict[height]) - leftmostIndex