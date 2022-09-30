/*
    A conveyor belt has packages that must be shipped from one port to another within days days.

    The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

    Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within 'days' days.

*/


/*
    Another variation of Allocate Minimum number of pages problem
*/


// Helper Method to check if a particular minimum capacity is valid or not
const isValidScheme = (weights, leastCapacity, days) => {
    let daysCount = 1;
    let capacity = 0;
    
    for(let i = 0; i < weights.length; i++){
        capacity += weights[i];
        
        if(capacity > leastCapacity){
            daysCount++;
            capacity = weights[i];
        }
    }
    
    if(daysCount > days){
        return false;
    }
    
    return true;
}


// Actual Logic
const shipWithinDays = (weights, days) => {
    let start = Math.max(...weights);
    let end = weights.reduce((a,b) => a + b);
    let result = -1;
    
    while(start <= end){
        let mid = Math.trunc(start + ((end - start))/2);
        
        if(isValidScheme(weights,mid,days)){
            result = mid;
            end = mid - 1;
        } else{
            start = mid + 1;
        }
    }
    
    return result;

}
