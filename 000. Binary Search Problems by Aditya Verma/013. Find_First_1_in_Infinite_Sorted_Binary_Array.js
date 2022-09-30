/*

    We are given a binary sorted array that is infinite. Binary means it only has 0 and 1. 

    WE have to find the first occurance of 1. 

    e.g. 0,0,0,0,0,0,1,1,1,1,1........ so on

    We don't know the length so we cannot directly apply Binary search as we cannot find the end.

    So, we will use the same concept as searching in an infinite array. i.e., start with start = 0, end = 1 and then keep checking if the element at end index is equal or greater than the element we need to find. Here, we have only 0 and 1s, so we just need to check if element at end is 1 or not. If it is not 1, start = end, end = end * 2

    If it is 1, save its index in some variable and now search before it for any other 1. If there is 1 before it, keep saving its index until we get 0 and so in the end, we will get the first index of 1.

*/


const firstOccurance = (arr, start,end) => {
    let index = -1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));
        
        if(arr[mid] === 1){
            index = mid;
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }

    return index;
}


const findFirstOne = (arr) => {
    let start = 0;
    let end = 1;

    while(arr[end] !== 1){
        start = end;
        end = end * 2;
    }

    return firstOccurance(arr, start, end);
}

console.log(findFirstOne([0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,]))
