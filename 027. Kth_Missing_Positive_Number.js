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

   And to find count of missing numbers we can do -

   last element in array - length of array.

   e.g. in arr = [1,2,4]

   last element = 4
   length of array = 3
   so, count of missing numbers = 4 - 3 = 1 < k

   e.g. arr = [2,3,4,7,11] and k = 5

    last element = 11
    length of array = 5
    count of missing numbers = 11 - 5 = 6

    since 6 is not less than 5 that means, the 5th missing number will be present in the range of the elements in array only. We don't need to search outside the array.


    ---------------------------------------------------

    In case we have to search outside the array, we can simply find the missing number by doing -> 
    
    (last element in array + k) - count of missing numbers

    e.g.arr = [1,2,3,4] , k = 2;

    last element = 4
    k = 2
    
    Since count of missing number = 0 and 0 < k that means we need to search outside the range of array elements

    So, 2nd missing number = 4 + 2 - 0 => 6

    arr = [1,2,4] , k = 2;
    last element = 4
    since count of missing numbers = 1 and 1 < k that means we need to search outside the range of array elements

    so, 2nd missing number = 4 + 2 - 1 => 5

    -------------------------------------------------
    We can use all of this in our Binary Search logic.
   
    so initially, we have start = 0 and end = last index of array
    we find mid

    now, we need to check if till this mid position, do we have count of missing numbers >= k or not. If yes, that means we will find our missing number on the left side of mid only. Otherwise, we will find it after the mid.

    to check count, again we can do -> mid element - expected mid

    i.e., arr[mid] - (mid + 1);

    Finally, there will be a case when loop terminates as end becomes less than start. At that case, our end will point to the largest number that is just smaller than the missing number we want to find. And there, we can simply use the formula - 

    (arr[end] + k) - (count of missing)

    Because at that time, we will do what is did in case of [1,2,3,4] i.e., search outside of this array by doing -> 
    
    last element + k - count of missing.


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

    //After loop ends, 'end' will point to the largest element in the array less than kth missing element. So, assuming that end is the last element of array, we can simply find the kth missing element using the formula -> last element + k - (count of missing elements till last element);
           
    let missingCount = arr[end] - (end + 1); //current Last - expected last

    return end === -1 ? k : arr[end] + k - missingCount;

};