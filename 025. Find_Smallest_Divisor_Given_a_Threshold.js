/*
    Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

    Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

*/


//Another variation of previous problems. Here, we know that the minimum value for a divisor can be 1 and the maximum can be the max number in the array. And for the helper method, we just need to check if the sum of array after each element is divided by the divisor is <= threshold or not. 


// Helper method
const isValid = (nums, divisor, threshold) => {
    let sum = 0;
    
    nums.forEach(num => {
        sum += Math.ceil(num/divisor);
    })
    return sum <= threshold;
}

// Main Logic
const smallestDivisor = (nums, threshold) => {
    let start = 1;
    let end = Math.max(...nums);
    let result = -1;
    
    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));
        
        if(isValid(nums, mid,threshold)){
            result = mid;
            end = mid - 1;
        } else{
            start = mid + 1;
        }
    }
    
    return result;
};
