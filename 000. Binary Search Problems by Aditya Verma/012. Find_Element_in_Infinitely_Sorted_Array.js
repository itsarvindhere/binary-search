/*

    An Infinitely sorted array does not have an end i.e., we do not know what is the size of that array. We are asked to find an element in an Infinitely Sorted Array. 

    We will use Binary Search but how? Since in BS, we set start and end indexes initially and search between those. But here, end cannot be found directly since we do not know the length of the array. 

    So, for that, initially, we take start as 0th index and end as the 1st index. And now, we check whether the element to find lies between start and end or not. i.e., whether element <= arr[end] or not

    If not that means we need to increment our end. So we can do end = end * 2. and set start = previous end

    Again we check if the element is <= arr[end] or not. There will be one case when 

    element will be <= arr[end] at that, we can apply Binary Search with our start and end indexes already set with the above process.

    So basically, we are finding the portion of array from an infinite array that includes the element to find.

*/

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

const findElementInInfinitelySortedArray = (arr,key) => {
    let start = 0;
    let end = 1;
    
    while(key > arr[end]){
        start = end;
        end = end * 2;
    }

    // Apply Binary Search Now
    return binarySearch(arr, key, start, end);
}
