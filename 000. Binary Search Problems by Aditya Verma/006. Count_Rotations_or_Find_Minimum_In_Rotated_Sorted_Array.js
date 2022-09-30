/*

    Lets say array is given as -> [11,12,15,18,2,5,6,8]

    So, we have to find how many times the array is rotated. If we notice, the index of minimum element is 4. And the number of rotations are also 4. That means Number of rotations = index of min element.
    
    But, how to find the minimum element in an array in log n time? 
    Linear search =  O(n)
    Binary Search = O(log n) So we have to use Binary Search to find the min index in a rotated sorted array


    1. What is the condition for an element to be the minimum?
    -> As we see above, 2 is minimum because on its left and on its right, there are bigger elements. Hence, an element is minimum in a sorted array if element on its left is greater or equal and also on its right. 


    2. If we did not get minimum element at mid, how to choose which way to move now? On left or right?
    -> Lets take above example. Initially, start = 0, end = 7, so mid = 3

    At mid we have 18. Since 15 < 18 and 2 < 18. That means above condition is not satisfied so 18 is not smallest. Hence we need to now move either to left of 18 or right of 18
        
    NOTE!!!
    There will be cases when our mid is at the 0th index or at the last index in that case, mid - 1 or mid + 1 will result in index out of bounds. So to avoid that, we set mid - 1 to the last index in case mid = 0 and mid + 1 to the first index if mid = last index. So we are assuming that we have a circular array. 

    If we compare the start element to mid. We see that start element is 11. mid is 18. And start element is smaller than the mid. That means the array on the left side is sorted. If we compare the right side, the element at the end is 8 and the element at mid is 18. Since the 8 < 18 that means the right side array is not sorted ([18,2,5,6,8]) So, we will find our min element in the unsorted array only.

    Hence, when mid is not minimum, check if the start <= mid or not. If it is, then start = mid + 1, else, end = mid - 1


    EDGE CASES ---->

    Lets take an array -> [4,5,6,7,0,1,2]

    Here, start = 0, end = 6, mid = 3
    arr[mid] = 7. Is 7 minimum? NO! Because 6 it not > 7 and 0 is not > 7. So we now need to move to either left or right.

    We see that start element is 4 and mid is 7. Since start <= mid that means left is sorted. So start = mid+ 1 => 4

    new mid = 5

    element at 5 is 1. It is not minimum because 0 is not > 1

    Now we need to decided whether to go to left side or right side. 

    We see that start element is 0 and mid element = 1. 0 <= 1. So with ths logic we should go to the right side, right? But that is wrong! Because if we see, min element is 0. If we go to right of 1, then we lose 0. So our logic is not right here. Hence, one more condition that we need to add is whether the start element is less than end element or not. If that is true, that means we need to search in left array.

    Hence to search on the left side of mid, we have two conditions -

    1. If start element < end element ,or,
    2. If start element is > mid element


    And that's it. This will be enough for the problem.


    SINCE WE ARE FINDING THE INDEX OF MINIMUM, THIS SAME CODE CAN BE ALTERED A BIT TO FIND THE MINIMUM IN A ROTATED SORTED ARRAY!!

*/


// Count of rotations = Index of the minimum Element in the array

const indexOfMinimumElement = (arr) => {
    let start = 0;
    let end = arr.length - 1;
    let minimum = 0;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));
        
        let prev = mid === 0 ? arr.length - 1 : mid - 1
        let next = mid === arr.length - 1 ? 0 : mid + 1;

        if(arr[prev] >= arr[mid] && arr[next] >= arr[mid]) {
            minimum = mid;
            break;
        }

        // Move towards unsorted part i.e., either left->mid or mid->right
        // To cover the edge case, also check if start element is less than end element. if it is, then also we need to look at left of mid
        if(arr[start] < arr[end] || arr[start] > arr[mid]){
            end = mid - 1;
        } else{
           start = mid + 1;
        }
    }

    return minimum;
};

let arr = [2,1];


console.log("Number of Rotations:", indexOfMinimumElement(arr))
