/*
    Given a sorted array of characters and a key. Find the smallest element that is greater than the given key.

    e.g. arr = ['a', 'c', 'f', 'h'];
        key = 'f';

    This means, find a smallest character in the array that comes after 'f'.

    Here, only 'h' comes after f so the result is 'h'.

    If we had - arr = ['a', 'c', 'f', 'h', 'i', 'j'];

    Then, 'h', 'i', 'j' come after 'f' but smallest of these is 'h'. 

    So, this is a variation of the Ceil of an element problem. The only difference is that we are dealing with characters here instead of numbers and when the mid is equal to key, we keep searching on the right of mid, instead of returning mid itself. 

    

*/


const nextAlphabeticalElement = (arr, key) => {
    let start = 0;
    let end = arr.length - 1;
    let next = -1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));
        if(arr[mid] > key){
            next = arr[mid];
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }

    return next;
}


let arr = ['a', 'c', 'f', 'h'];
let key = 'f';
console.log(nextAlphabeticalElement(arr,key));
