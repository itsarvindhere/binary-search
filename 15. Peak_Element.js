/*
    Given an unsorted array. Find and return the index of a peak element. An array can have multiple peak elements. If there are multiple, return any one index. 

    A peak element is the one that is greater than both of its neighbors (i.e.., left neighbour and right neighbour)

    e.g. arr = [5, 10, 20, 15];

    Here, 20 is the peak element because 20 > 10 and also 20 > 15. So its index is 2 and hence we return 2.

    It is an unsorted array but still, we can apply Binary Search on it. 
    
    So, initially, start = 0, end = 3 and mid = 1

    We see that arr[mid] = 10. Now, how to know if this is the peak element or not? As the problem statement says, peak means greater than element to its left and to its right.

    So, 
        arr[mid] > arr[mid - 1] => 10 > 5 => YES
        arr[mid] > arr[mid + 1] => 10 > 20 => NO

    So, 10 is not the peak element. Which means we either need to move to left side of 10 or to right side of 10. 

    How to decide that? Well, we have to see which side is more promising to have a peak element. On left of 10, we have 5. Because 10 is already bigger than 5. That means 5 can never be a peak element. But on the right side of 10 we have 20. Since 10 is smaller than 20, that means, 20 can be a peak element sicne one of its neighbours is smaller than it. So, we move to the side that looks more promising.

    This is the concept of "Binary Search on Answer"
    
    What we are essentially doing is going in the direction of the rising slope(by choosing the element which is greater than current). How does that guarantee the result? Think about it, there are 2 possibilities - 
        a) rising slope has to keep rising till end of the array 
        b) rising slope will encounter a lesser element and go down.

    In both scenarios, we will have an answer. 
    In a) the answer is the end element because we take the boundary as -INFINITY 
       b) the answer is the largest element before the slope falls. 

*/

/*
    NOTE - If Problem says element should be 'strictly greater' than neighbours, just replace >= with >
*/
const peakElement = (arr) => {
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

    return 0;
}


let arr = [1];

console.log("Peak Element's Index is: ", peakElement(arr))