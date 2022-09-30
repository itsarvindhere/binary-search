# PROBLEM STATEMENT

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# EXAMPLE

    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8
    Explanation: There are 8 negatives number in the matrix


# APPROACH

The straightforward way is to do a linear search and go through each row and count negatives. But that is an O(m * n) solution and not efficient.

Since the matrix is sorted, why not use Binary Search instead.

One way is to use binary search on each row and count number of negatives as soon as we find the first negative since the row is sorted, all numbers after it are also negative.

And even better approach is to start from bottom left corner of matrix because at that point, all elements on right are smaller and all elements on top are bigger so we do not need to go for bigger elements at all. 



