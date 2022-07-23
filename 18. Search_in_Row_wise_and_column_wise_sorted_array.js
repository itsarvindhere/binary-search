/*

    Given an array (2D Array) that is row wise sorted and column wise sorted. Search an element in this array. 

    Since the element is sorted, we can think of using Binary Search. But how to use it? 

    APPROACH - 

    1. Consider mid to be the top right element initially. i.e., if each row has m elements, then initially, mid = arr[0][m - 1];

    2. Now, compare the element that we want to find with mid. If it is same, return this position. Otherwise, we need to see if element is less or greater.

    3. If key > mid. That means, we need to search elements greater than mid for our key. And elements greater than mid will be in the column below mid. So we go downwards by incrementing i. 

    4. If key < mid. That means, we need to search elements less than mid for our key. And elements less than mid will be in the row before mid. So we go backwards by decrementing j. 

    5. Do this until we find the position.


    WHY WE STARTED FROM TOP RIGHT? 

    Because if we see, from top right, there are two possibilities. On the bottom side, all elements are greater and on the left side, all elements are smaller. so we can choose one path and neglect the other. This is something we cannot do if we start from first because at i = 0 and j = 0, whatever element is present, its right side will have all elements greater than it and also its bottom. So we cannot choose which way to go because on both sides, elements are greater than current element.

*/


const binarySearchOnTwoDimensionalSortedArray = (arr, key) => {
    let start = 0;
    let end = arr[0].length - 1;
    while(start  < arr.length && end >= 0){
        let mid = arr[start][end];
        if(mid === key){
            return [start,end];
        }
        if(key > mid){
            start++;
        } else{
            end--;
        }
    }

    return -1;
}


let arr = 
[
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]

let key = 29;

console.log("Position of " + key + " in the array is:", binarySearchOnTwoDimensionalSortedArray(arr,key))
