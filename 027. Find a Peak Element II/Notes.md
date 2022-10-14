# PROBLEM STATEMENT

A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.


# EXAMPLE

    Input: mat = [[1,4],[3,2]]
    Output: [0,1]

Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

# BRUTE FORCE APPROACH - O(MN)

The brute force approach is pretty straightforward. For each row, do a linear scan and for each element, check if it is peak. As soon as we get a peak, return the indices of that row and column.

# BINARY SEARCH APPROACH - O(MLogN)

Think about it. If an element is not peak, that means, it is probably because either the element on its left is bigger, or element on its right is bigger. Or if both left and right are not bigger, then it is not peak because the elements on its top or bottom are bigger.

So, if some element is not the peak element and the element on its left is also smaller than it, then it makes sense to search for a peak element on right because there we have a bigger probability of finding a peak element than on the left side.

In this way, we can discard one half each for every non-peak element and to implement this idea, we use Binary search.

Also, there will be scenarios when both elements on right and left are bigger than the current element. In that case, it makes sense to move towards the element that is bigger of two. As we have a bigger chance to find peak element on that side.

And if the mid element is bigger than both left and right elements but is still not the peak, that's because the element on bottom is bigger. Why not top? Because we are performing Binary search starting from the first row. So there can never be a case where any element on top of a mid element can be the peak element because we have already checked it when we were at the previous row.

