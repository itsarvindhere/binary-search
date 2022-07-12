/*
    Suppose we have an array = [2,4,10,10,10,18,20];

    If we want to search 10, we apply binary search and we find mid == element so index = 3. But, in this problem, we have to find the 'First Occurance' & 'Last Occurance' of an element.
    
    In above array, first occurance of 10 is at index 2 and last occurance of 10 is at index 4. 

    So we have to do some extra operation apart from normal binary search as soon as we find that element at mid. We have to check if the element at mid is also at its first occurance or not.

*/

const firstOccurance = (arr, el) => {
    let start = 0;
    let end = arr.length - 1;
    let result = -1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start) / 2)); //Avoid int overflow
        if(el === arr[mid]){
            result = mid;
            end = mid - 1;
        } else if (el > arr[mid]){
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    return result;
}

const lastOccurance = (arr, el) => {
    let start = 0;
    let end = arr.length - 1;
    let result = -1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start) / 2)); //Avoid int overflow
        if(el === arr[mid]){
            result = mid;
            start = mid  + 1;
        } else if (el > arr[mid]){
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    return result;
}

let arr = [2,4,10,10,10,18,20];

console.log("First and last index of 10 in arr: ", [firstOccurance(arr,10), lastOccurance(arr,10)])