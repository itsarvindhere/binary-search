// Binary Search Method
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

// Using the Method
let arr = [1,2,3,4,5,6,7,8,9,10];
console.log("Index of 6 in the Array is: ", binarySearch(arr,6))