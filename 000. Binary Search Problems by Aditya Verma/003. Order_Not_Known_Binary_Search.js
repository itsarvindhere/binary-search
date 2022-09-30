//Binary Search on Ascending Order Array

const binarySearch = (arr, el) => {
    let start = 0;
    let end = arr.length - 1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start) / 2)); //Avoid int overflow
        if(el === arr[mid]){
            // Element found. Return mid index
            return mid;
        } else if (el > arr[mid]){
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    // Element not found in the array
    return -1;
}

// Binary Search on Descending Order Array
const binarySearchOnReverseSortedArray = (arr, el) => {
    let start = 0;
    let end = arr.length - 1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start) / 2)); //Avoid int overflow
        if(el === arr[mid]){
            // Element found. Return mid index
            return mid;
        } else if (el > arr[mid]){
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    // Element not found in the array
    return -1;
}


// We have to apply binary search on an array to find an element but we don't know in what order the array is sorted. It can be sorted in ascending or descending.

const binarySearchOnOrderNotKnownArray = (arr,el) => {
    // Find the sort order
    let isAscending = true;
    for(let i = 1; i < arr.length; i++){
        if(arr[i] < arr[i - 1]){
            isAscending = false;
            break;
        }
    }

    return isAscending ? binarySearch(arr,el) : binarySearchOnReverseSortedArray(arr,el)
}



let arr1 = [1,2,3,4,5,6]
let arr2 = [6,5,4,3,2,1]

console.log(binarySearchOnOrderNotKnownArray(arr1, 4))
console.log(binarySearchOnOrderNotKnownArray(arr2,4))
