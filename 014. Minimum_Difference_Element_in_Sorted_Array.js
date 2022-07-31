/*
    Given an array and a key. Find an element in the array which results in the minimum absolute difference when substracted from the given key.

    e.g. arr = [4,6,10] and key = 7.

    If we substract each element with 7 and check the absolute difference - 

    |4 - 7| => 3
    |6 - 7| => 1   <- THis is the minimum difference hence, return 6. 
    |10 - 7| => 3


    e.g. arr = [1,3,8,10,13] key = 12

    |1 - 12| = 11
    |3 - 12| = 9
    |8 - 12| = 4
    |10 - 12| = 2
    |13 - 12| = 1 <- This is the minimum hence return 13.


    So, from these two examples, we can see that the element that will result in the minimum difference is the element that is closest to the key. e.gg, 6 in case of key = 7 and 13 in case of key = 12.

    Hence, we have to find the ceil and floor of an element in the given array.

    e.g. for arr = [4,6,10] and key = 7

    ceil = 10
    floor = 6

    And now, we just need to see which one results in the minimum difference 

    |10 - 7| = 3
    |6 - 7| = 1

    So here, floor results in minimum difference hence return the floor. 

    -------------------------------------------------

    for arr = [1,3,8,10,13] key = 12

    ceil = 13
    floor = 10

    And now, we just need to see which one results in the minimum difference 

    |13 - 12| = 1
    |10 - 12| = 2

    So here, ceil results in minimum difference hence return the ceil. 

    -----------------------------------------------

    Also, if the array contains the key itself, then in that case, the minimum difference element will be the key itself. 

    e.g. arr = [1,3,8,10,12,13] key = 12

    Here, array has 12. So 12 - 12 = 0 which is minimum that we can get. Hence in that case, return 12.

*/


// Floor and Ceil of an element
const floorAndCeilOfElement = (arr, key) => {
    let start = 0;
    let end = arr.length - 1;
    let ceil = -1;
    let floor = -1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));

        if(arr[mid] === key){
            return [key,key];
        }

        if(arr[mid] > key){
            ceil = arr[mid];
            end = mid - 1;
        }

        if(arr[mid] < key){
            floor = arr[mid]
            start = mid + 1;
        }
    }
    return [floor, ceil];
}

//Main Logic
const minimumDifferenceElement = (arr, key) => {
    let [floor,ceil] = floorAndCeilOfElement(arr,key);

    let diff1 = Math.abs(floor - key);
    let diff2 = Math.abs(ceil - key);

    return diff1 < diff2 ? floor : ceil;
}


let arr = [2,3,8,10,13];
let key = 14;
console.log(minimumDifferenceElement(arr,key))
