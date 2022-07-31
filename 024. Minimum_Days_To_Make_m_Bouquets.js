/*
    You are given an integer array bloomDay, an integer m and an integer k.

    You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

    The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

    Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

*/

//This is also a variation of previous problems. Here as well, we need to use Binary search because it is monotonous. If we are able to find any value 'day' such that we are able to make m number of bouquets if we wait 'day' number of days for the flowers to bloom, then any number of days that are more than 'day' will also satisfy.

/*

    Here, we know that the minimum that we may have to wait is 1 day because it is given that 1 is the minimum value in array. So our start = 1. 

    And the maximum that we may have to wait is the max value in the array because lets say we have

    arr = [1,10,3,10,2]

    This means, 10 days is the maximum number of days we need to wait to make sure all the flowers have bloomed. 

    Hence, our binary search runs between 1 and 10 for above array.


*/


// Function that checks if a particular day value can be a candidate to become minimum days to wait to make m bouquets
const isValid = (bloomDay, minDaysToWait, m, k) => {
    let bouquets = 0;
    let flowers  = 0;
    
    for(let i = 0; i < bloomDay.length; i++){ 
        if(bloomDay[i] <= minDaysToWait){
            flowers++;
        } else{
            flowers = 0;
        }
        
        if(flowers === k){
            bouquets++;
            flowers = 0;
        }
        
    }
            
    return bouquets >= m;
    
}


// Main logic
const minDays = (bloomDay, m, k) => {
    let start = 1;
    let end = Math.max(...bloomDay);
    let result = -1;
    
    //Not enough flowers
    if((m * k) > bloomDay.length) return -1;
    
    while(start <= end) {
        let mid = Math.trunc(start + ((end - start)/2));
        if(isValid(bloomDay, mid, m, k)) {
            result = mid;
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    
    return result;
    
};
