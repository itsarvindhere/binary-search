/*
    We are given a nearly sorted array.

    A nearly sorted array is an array where an element can either be at the correct position or correct position - 1 or correct position + 1.

    e.g. let arr = [5,10,30,20,40];

    Here, 30 is at 2nd index but ideally, if this array is sorted, it should be at 3rd index. That means, it is at required index - 1 index.
    Similarly, 20 is at required index + 1. 

    APart from these two, all others are at correct place so, this is a nearly sorted array. 

    Hence, when we apply Binary Search at this array, then along with checking if element === mid or not, we also need to check if element === mid - 1 and elemenet === mid + 1. 

    And if it is not equal to any of the three indexes, we need to move to either left or right. If we go to left, then end becomes mid - 2 and if we go to right, start becomes mid + 2

    here we increment/decrement by 2 because we have already checked mid - 1 and mid + 1

*/



const findElement  = (arr, el) => {
    let start = 0;
    let end = arr.length - 1;
    
    while(start <= end){
        let mid = start + ((end - start)/2);

        if(arr[mid] === el){
            return mid;
        } 
        
        if (((mid - 1) >= start) && arr[mid - 1] === el){
            return mid - 1;
        }
        
        if(((mid + 1) <= end) && arr[mid + 1] === el){
            return mid + 1;
        }

        if(el > arr[mid]) {
            start = mid + 2;
        } else{
            end = mid - 2;
        }
    }

    return -1;
}


let arr = [5,10,30,20,40];
console.log(findElement(arr,5))