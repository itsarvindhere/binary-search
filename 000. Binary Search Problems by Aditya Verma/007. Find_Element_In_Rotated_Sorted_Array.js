// Method to find the index of minimum element in the rotated sorted array
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

        if(arr[start] < arr[end] || arr[start] > arr[mid]){
            end = mid - 1;
        } else{
           start = mid + 1;
        }
    }

    return minimum;
};

// Binary Search Method
const binarySearch = (arr,el,start,end) => {
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



// Main Logic to find element in a rotated sorted array
const findElement = (arr, target) => {
    let indexOfMin = indexOfMinimumElement(arr);
    let location = -1;

    if(arr[arr.length - 1] < target){
        location = binarySearch(arr, target, 0, indexOfMin - 1);
    } else{
        location = binarySearch(arr, target, indexOfMin, arr.length - 1)
    }

    return location;
    
}

let arr = [5,1,3];
console.log("Index of 3 in the array is :", findElement(arr,3))
