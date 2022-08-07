/*
    Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

    An integer a is closer to x than an integer b if:

        |a - x| < |b - x|, or
        |a - x| == |b - x| and a < b

*/


/*
                BRUTE FORCE APPROACH

    Since it is given that the array is 'SORTED', first thing that should come to mind is Binary Search. 

    But lets see how to do it with a brute force approach

    e.g. arr = [1,2,3,4,5] if x = 3 and k = 4

    First ,we want to see where the element x is in array. here we are assuming that X is present in the array. But it may not be the case with some test cases. Anyways, 

    we do a linear search and see that x = 3 is at index = 2. Since it is the closest since difference is 0, we include it in array.
    
    result = [3]

    Now, we know that the closest to 3 are its neighbors.

    So we keep two pointers. One pointing to left neighbor and other to right neighbor. 

    left = 2
    right = 4

    Then we see which one has least abs difference. 
    If both have same diff, choose the element that is smaller.

    abs diff 1 = |2 - 3| = 1
    abs diff 2 = |4 - 3| = 1

    since difference is same, choose 2 since 2 < 4. 

    result = [3,2]

    And now we update our left pointer to point to the previous element after 2.

    left = 1
    right = still 4

    Again, comptue abs diff -

    abs diff 1 = |1 - 3| = 2
    abs diff 2 = |4 - 3| = 1

    diff2 < diff1 so choose 4.

    result = [3,2,4]

    And since we got our k closest numbers, just sort this result array and return.
*/

/*
        BINARY SEARCH

        Since the array is sorted, we can reduce the time complexity from O(n) to O(logn) while searching.

        And we can do all the process again with two pointers.
*/

 /*



            BUT, what if the target is not in the array?

            e.g. arr [ 1,2,3,4,5] x = -1, k = 3

            Here, we see that -1 is not present in the array. This means we cannot do the same thing we did in above methods. We need to change our solution.

            If the target does not exist in array, we simply find the closest element to the target value in the array.

            e.g. in above case, the closest to -1 is 1. 

            And then, we can still do the two pointer approach. 

            arr = [1,2,3,4,8]
            x = 6
            k = 4

            Here, 6 does not exist in the array. But, what is the closest element to 6? Well, we can see that they are 4 and 8 because both have abs difference of 2. It is given in problem that if abs diff is same, choose the smaller value.

            So in this case, closest to 6 is 4. And now from there on, we again do the same thing with two pointers.


*/

const findClosestElements = (arr, k, x) => {
    let start = 0;
    let end = arr.length - 1;

    let closest = []; //This array stores the closest elements to x
    let closestIndex = -1; //This stores the index of the element closest to x. It can be x itself if present in the array.
    
    let floor = -1; //Largest element that is smaller than x
    let ceil = -1; //Smallest element that is larger than x
    
    
    while(start <= end) {
        let mid = Math.trunc(start + ((end - start)/2));
        
        if(arr[mid] === x){
            closestIndex = mid;
            break;
        }
        
        if(arr[mid] < x){
            floor = mid;
            start = mid + 1;
        } else{
            ceil = mid;
            end = mid - 1;
        }
    }
        
    //If x is not present in the array, we have to select the closestIndex as the element closest to X in array
    if(closestIndex === -1){
        
        if(arr[arr.length - 1] < x){ //If x is bigger than last element, that means closest to x is the last element since array is sorted
            closestIndex = arr.length - 1;
        } else if(arr[0] > x){ ///If x is smaller than first element, that means closest to x is the first element since array is sorted
            closestIndex = 0;
        } else{          
            let abs1 = Math.abs(arr[floor] - x);
            let abs2 = Math.abs(arr[ceil] - x);

            if(abs1 === abs2){ //if same abs difference, choose the smaller element i.e., floor
                closestIndex = floor;
            } else{
                closestIndex = abs1 < abs2 ? floor : ceil; //Choose the one that results in the least absolute difference
            }
        }

    }
    
    closest.push(arr[closestIndex]);
            

    // TWO POINTER APPROACH BEGINS FROM HERE
    let left = closestIndex - 1;
    let right = closestIndex + 1;
    
    while(closest.length < k){
        let abs1 = Math.abs(arr[left] - x);
        let abs2 = Math.abs(arr[right] - x);
        
        if(abs1 === abs2){
            closest.push(arr[left--]);
        } else{
            closest.push((abs1 < abs2 || right > arr.length - 1) ? arr[left--] : arr[right++]);
        }
    }
        
    closest.sort((a,b) => a - b); //Since we are asked to return a sorted array as result
    
    return closest;
    
};


/*
    ANOTHER APPROACH WITH BINARY SEARCH


    In this approach, instead of searching for the element that is closest to X, we will search for the whole window of k elements in the array. 

    (NOTE - MID WILL ALWAYS POINT TO LEFT MOST VALUE OF A WINDOW)

    e.g. arr = [1,2,3,4,5]
    x = 5, k = 2

    So, the size of the window is 2. We need to search the window with 2 elements that are closest to x.

    suppose we take the window of elements [3,4]. We might have some way to check if there can be a better window than this so we can look at either left side or right side.... e.g. window[2,3] or window [4,5] and so on...

    Since we want a window of length k = 2, we cannot make a window from last element as we would need one more element and that would go out of bounds. In simple words, our binary search will be from 0 to (length of array - k)

    Now, how do we see if a window is better than the previous one. 

    arr = [1,2,3,4,5]
    x = 5, k = 2

    Suppose our window is [3,4]

    Now, to check if [4,5] is a better window, what we can do is check if addition of 5 improves the closerness. If it does, that means, we will never find a better window to the left side. It will always be on the right side of [3,4] window.

    If 5 is not closer than 3, then we do the opposite. i.e., look for a better window on the left side of [3,4] window
    
    
    --------------------------------------------------------------
     arr = [1,2,3,4,5]
    x = 5, k = 2

    start = 0, end = arr.length - k => 5 - 2 => 3

    mid = 1, arr[mid] = 2

    Hence our window becomes [2,3] because we know the leftmost element of window is the mid element.

    Now, what we do is check if 2 is closer to 5 than the value that is jsut outside the window i.e., 4

    5 - 2 = 3
    5 - 4 = 1

    Obviously 4 is closer. This means, we can have a better window if we include 4 and discard 2. So we need to shift our window to right.
    
    In other words, we make start = mid + 1 = 2. end still points to index 3.

    arr[mid] = 3
    So the new window now is [3,4]

    Again, we do the same check. The element just outside of window is 5 so we check if 5 is closer to X than 3.

    5 -5 = 0
    5 - 3 = 2

    Yes! 5 is closer. Hence, that means if we include 5 in this window and discard 3, we have more closer elements. 

    start = mid + 1 = 2 + 1 = 3
    end = 3

    Mid = 3, arr[mid] 


    New window = [4,5]

    And since start and end are same now, that means this is our final solution -> [4,5]


*/

const findClosestElements2 = (arr, k, x) => {
    let start = 0;
    let end = arr.length - k;

    while(start < end) {
        let mid = Math.trunc(start + ((end - start)/2));

        /*
            NOTE - If we find absolute values for diff1 and diff2, it will fail in some test cases
            So, we have to do -> (x - mid value) and (mid + k value - x)

            To remember this, jsut remember that for right value i.e, for value just outside window (mid + k), X will be on right side of substraction. For left value i.e, value at leftmost point of window (mid). X will be on left side of substraction.
            
        */
        let diff1 = x - arr[mid];
        let diff2 = arr[mid + k] - x;

        if(diff1 > diff2) {
            left = mid + 1;
        } else{
            right = mid;
        }
    }

    let result = arr.slice(start, start + k);

    return result;

}