# PROBLEM STATEMENT

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

In simple words, find how many numbers are there in arr1 such that 
            |arr1[i]-arr2[j]| > d

# EXAMPLE

    Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
    Output: 2
    Explanation: 
        For arr1[0]=4 we have: 
        |4-10|=6 > d=2 - VALID
        |4-9|=5 > d=2  - VALID
        |4-1|=3 > d=2  - VALID
        |4-8|=4 > d=2  - VALID
        For arr1[1]=5 we have: 
        |5-10|=5 > d=2  - VALID
        |5-9|=4 > d=2  - VALID
        |5-1|=4 > d=2   - VALID
        |5-8|=3 > d=2  - VALID
        For arr1[2]=8 we have:
        |8-10|=2 <= d=2 - INVALID
        |8-9|=1 <= d=2 - INVALID
        |8-1|=7 > d=2 - VALID
        |8-8|=0 <= d=2 - INVALID

    Since there are only two valid values, output = 2

# APPROACH

The main thing we see when we want to check if Binary Search can be used in any problem is to see if there is any monotonically increasing or decreasing condition.

E.g. if there is any case such as - 
    If a smaller value is valid, all smaller values are valid
    or If a bigger value is valid, all are valid

Then we know that as soon as we know a smaller value is valid, there is no point to check for all smaller values. Or vice versa.


Here, we have the same situation.

If we sort the second array, we will get

        arr1 = [4,5,8]
        arr2 = [1,8,9,10]
        d = 2

Starting with 4,
We apply binary search on second array and get mid value as 8. And we see that the condition |4 - 8| > 2 is true.

Since 8 is > 4, it means any value  > 4 will be valid too so we don't need to check for values after 8. We just need to check for values on left of 8.

And the same case if it was other way around. e.g., if there was a smaller value than 4 in mid and it was valid, then all elements before mid would've been valid too. 