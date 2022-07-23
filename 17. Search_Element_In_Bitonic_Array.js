/*
    Given a Bitonic array, search the given element and return the index. Return -1 if not present

    Bitonic array means an array that is initially monotonically increasing and then it may be monotonically decreasing after one point. We need to find that one point which is the peak. 

    e.g. arr = [1, 3, 8 , 12 , 4, 2], key = 4

    If we want to search for 4, we have to return its index, which is 4. 

    But how to find? 

    If we see, before the peak index and after the peak index, we have sorted arrays.

    [1,3,8] and [4,2]

    And as we know, Binary Search is the best solution for searching in sorted arrays. Hence, we can apply Binary search on these two arrays and see which one has the element. if both don't have it, return -1 as the element is not in the array.

    Also, before doing this, we can check if the peak element is the key or not. if it is, return index of peak.

*/


// Method to find the peak index in the Bitonic Array
const peakElementInBitonicArray = (arr) => {
    let start = 0;
    let end = arr.length - 1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));

        if(mid > 0 && mid < arr.length - 1){
            if(arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1]){
                return mid;
            } else{
                if(arr[mid] > arr[mid - 1]){
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        } else if(mid === 0){
            if(arr[mid] > arr[mid + 1]){
                return mid;
            } else{
                start = mid + 1;
            }     
        }else{
            if(arr[mid] > arr[mid - 1]){
                return mid;
            } else{
                end = mid - 1;
            }
        }
        
    }

    return arr[arr.length - 1];
}

// Binary Search
const binarySearch = (arr, start, end, key, order) => {

    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));

        if(arr[mid] === key){
            return mid;
        } else if (arr[mid] < key){
            if(order == 'asc'){
                start = mid + 1;
            } else{
                end = mid - 1;
            }
        } else {
            if(order == 'asc'){
                end = mid - 1;
            } else{
                start = mid + 1;
            }
        }
    }

    return -1;
}


const indexOfElementInBitonicArray = (arr, key) => {
    let peakIndex = peakElementInBitonicArray(arr);

    if(arr[peakIndex] === key) return peakIndex;

    let lIndex = binarySearch(arr, 0, peakIndex - 1, key, 'asc');
    let rIndex = binarySearch(arr, peakIndex + 1, arr.length - 1, key, 'desc');

    if(lIndex !== -1){
        return lIndex;
    } else if (rIndex !== -1){
        return rIndex;
    }

    return -1;

}


let arr = [1,3,8,12,4,2];
let key = 12;

console.log("Index is:", indexOfElementInBitonicArray(arr,key))