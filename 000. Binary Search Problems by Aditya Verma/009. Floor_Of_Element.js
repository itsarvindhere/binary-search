/*

    Given a sorted array and an element, Find the floor of that element in the given array.

    Floor of an element is the greatest element that is smaller than or equal to given element.

    e.g. [1,2,3,4,6,7,8,10], element = 5

    SO, we have to find floor of 5 in this array. 

    As we see, the elements smaller than or equal to 5 are 1,2,3,4
    Out of these, the greatest element = 4

    Hence floor or 5 in this array = 4.

    Since we are given a sorted array, we can use Binary Search on this array.

    The only thing we need to do is, if the mid is less than element, that means we need to make it the floor and keep searching more any element that is greater than this new floor. 

    Also if the mid itself is the element, return that. 

*/


const floorInSortedArray = (arr,el) => {
    let start = 0;
    let end = arr.length - 1;
    let floor = -1;


    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));

        if(arr[mid] === el){
            return el;
        } else if (arr[mid] > el){
            end = mid - 1;
        } else {
            floor = arr[mid]; //Make this the new floor since it is smaller than the given element
            start = mid + 1;
        }
    }

    return floor;
}

let arr = [1,2,3,4,8,10,12,19];
let el = 5;

console.log("Floor is:", floorInSortedArray(arr,el))
