/*

    Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

    Return the kth positive integer that is missing from this array.


    e.g. arr = [2,3,4,7,11] and k = 5

    Here the missing numbers are [ 1, 5, 6, 8, 9, 10, 12, 13, ... . .]
    

    Out of these, 5th number is 9. Hence, we need to return 9 in this case.


    e.g. arr = [1,2,3,4] , k = 2;

    Here, there are no missing numbers in the array ityself but since we are asked for 4th missing number, that means missing numbers after 4. 

    i.e., [5,6,7,8,9,10,11....]

    Here, 2nd number is 6. So, return 6 in this case.



    Since it is already told that this is a strictly increasing array or sorted array, we can make use of Binary Search here. 

    In the first case, we saw that the number was in the range of elements of array itself. But in 2nd case, number was outside the range of array. So, how can we check whether to search inside the array or outside the array?


    We see that it depends on the missing numbers count. e.g.
    arr = [1,2,3,4] , k = 2;
    Here, there are no msising numbers in the array. Hence we have to search outside the array. Even if there was one number missing e.g.

    arr =  [1,2,4], k = 2 

   Even then, we had to find outside the array because we want 2nd missing number and in this array only one number is missing.

   Hence, we have to search outside the array if the count of missing numbers < k

   And to find count of missing numbers till any index we can do -

   (element at that index currently - element we expect at that index)

   e.g. in arr = [1,2,4]

   at last index, we have 4. 
   But if we take a look at array, since there rae three elements, ideally there should be [1,2,3] so last element should be 3

   Hence here, missing elements till last index = 4 - 3 = 1

   e.g. arr = [2,3,4,7,11] and k = 5

    last element = 11
    Expected = 5

    count of missing numbers = 11 - 5 = 6

    since 6 is not less than 5 that means, the 5th missing number will be present in the range of the elements in array only. We don't need to search outside the array.


    ---------------------------------------------------

    In case we have to search outside the array, we can simply find the missing number by doing -> 
    
    last index with largest element smaller than kth missing element + k + 1

    e.g.arr = [1,2,3,4] , k = 2;

    last element = 4
    k = 2
    
    Since count of missing number = 0 and 0 < k that means we need to search outside the range of array elements

    So, 2nd missing number = 3 + 2 + 1 = 6 (because 3 is the index of 4 which is the last element smaller than kth missing element = 6)

    Or to understand in other way, since there are 0 missing numbers till last element, that means the array has no missing elements. We can simply add k to the last element to get the kth element in the sequence. We add 1 because of 0 based indexing.

    arr = [1,2,4] , k = 2;
    last element = 4
    since count of missing numbers = 1 and 1 < k that means we need to search outside the range of array elements

    so, 2nd missing number = 2 + 2 + 1 => 5 (here, index of last element = 2)

    -------------------------------------------------
    We can use all of this in our Binary Search logic.
   
    so initially, we have start = 0 and end = last index of array
    we find mid

    now, we need to check if till this mid position, do we have count of missing numbers >= k or not. If yes, that means we will find our missing number on the left side of mid only. Otherwise, we will find it after the mid.

    to check count, again we can do -> mid element - expected mid

    i.e., arr[mid] - (mid + 1);

    Finally, there will be a case when loop terminates as end becomes less than start. At that case, our end will point to the largest number that is just smaller than the missing number we want to find. And there, we can simply use the formula - 

    end + k + 1

    Because at that time, we will do what is did in case of [1,2,3,4] i.e., search outside of this array by doing -> 
    
    (index of largest element just smaller than kth + k + 1)


    SO, when our loop ends, we assume that our array is from 0 to end index only. And so, our missing element lies outside of this array.

    Basically, we are using binary search to find that place in the array before which the missing number cannot be found.

*/


const findKthPositive = (arr, k) => {
    
    let n = arr.length;
    let start = 0;
    let end = n - 1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));
        let countOfMissingNumbers = arr[mid] - (mid + 1); //Current Mid element - expected mid element
        if(countOfMissingNumbers < k ){
            // We need to look at right side of mid because till mid, missing numbers are less than k so obviously we cannot find kth missing number on left side of mid
            start = mid + 1;
        } else{
            end = mid - 1;
        }
        
    }

    //After loop ends, 'end' will point to the largest element in the array less than kth missing element. So, assuming that end is the last element of array, we can simply find the kth missing element using the formula -> (end + k) + 1. We did +1 because index starts from 0 and here we are dealing with numbers starting from 1.

    // To handle corner cases where end will become -1, that means the missing number is k itself
    /*

        e.g. arr = [2], k = 1
        So we need 1st missing number. If we run the loop, end will eventuall be -1. So in that case, we return k i.e., 1. because here 1 is the first missing number

    */

    return end === -1 ? k : end + k + 1;

};