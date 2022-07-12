/*
    Given a sorted array and an element, Find the ceil of that element in the given array.

    Ceil of an element is the smallest element that is greater than or equal to given element.

    e.g. [1,2,3,4,6,7,8,10], element = 5

    SO, we have to find ceil of 5 in this array. 

    As we see, the elements greater than or equal to 5 are 6,7,8,10
    Out of these, the smallest element = 6

    Hence ceil of 5 in this array = 6.

    Since we are given a sorted array, we can use Binary Search on this array.

    The only thing we need to do is, if the mid is greater than element, that means we need to make it the ceil and keep searching for any element that is smaller than this new floor but greater than the element. 

    Also if the mid itself is the element, return that. 
*/

const ceilInSortedArray = (arr,el) => {
    let start = 0;
    let end = arr.length - 1;
    let ceil = -1;


    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));

        if(arr[mid] === el){
            return el;
        } else if (arr[mid] > el){
            ceil = arr[mid]; //Make this the new ceil since it is greater than the given element
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }

    return ceil;
}

let arr = [1,2,3,4,6,8,10,12,19];
let el = 5;

console.log("Ceil is:", ceilInSortedArray(arr,el))