/*

    Given a sorted array of n elements, possibly with duplicates, find the number of occurrences of the target element.

    Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8
    Output: 3

    Because 8 occurs 3 times.

    We want to do it in logn time. 

    That means we use Binary Search for this.

    Because we already know how to find firstOccurance and lastOccurance of an element, we can easily find how many times an element is there in an array based on those two values

    e.g. in above array, 
        index of first occurance of 8 -> 2 
        index of last occurance of 8 -> 4

        So, number of times it occurs in array = (lastOccurance - firstOccurance) + 1;
        We added 1 becase as we know, index starts from 0.

    if element is not in array we know firstOccurance and lastOccurance will be -1. In that case we can simply return -1.
        
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


const countOfElementInSortedArray = (arr,target) => {
    const first = firstOccurance(arr,target);
    const last = lastOccurance (arr,target);

    if(first === -1 || last === -1) return -1;
    return last - first + 1;
}


let arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42];
let target = 8;

console.log("Count of 8 in array: ", countOfElementInSortedArray(arr,target))
