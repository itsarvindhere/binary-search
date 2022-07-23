/*
    Given a Bitonic array, find the peak element.

    Bitonic array means an array that is initially monotonically increasing and then it may be monotonically decreasing after one point. We need to find that one point which is the peak. 

    It is a variation of the Finding Peak element problem where we used the "Binary Search on Answer"
    concept.

*/

const maxInBitonicArray = (arr) => {
    let start = 0;
    let end = arr.length - 1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));

        if(mid > 0 && mid < arr.length - 1){
            if(arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1]){
                return arr[mid];
            } else{
                if(arr[mid] > arr[mid - 1]){
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        } else if(mid === 0){
            if(arr[mid] > arr[mid + 1]){
                return arr[mid];
            } else{
                start = mid + 1;
            }     
        }else{
            if(arr[mid] > arr[mid - 1]){
                return arr[mid];
            } else{
                end = mid - 1;
            }
        }
        
    }

    return arr[arr.length - 1];
}


let arr = [1,3,8,10,12]

console.log("Peak element in the Bitonic array is:", maxInBitonicArray(arr))