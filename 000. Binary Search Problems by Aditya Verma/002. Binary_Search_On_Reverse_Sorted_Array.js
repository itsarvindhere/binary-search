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

let arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];

console.log("Index of 4 in the array is: ", binarySearchOnReverseSortedArray(arr,4))
