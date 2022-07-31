/*
    Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

    Write an algorithm to minimize the largest sum among these m subarrays.

*/

//This is again a variation of Allocate Minimum number of pages problem.


// Helper Method to check if a particular minimum SUM is valid or not
const isValidScheme = (nums,minSum,m) => {
    let countOfSubarrays = 1;
    let sum = 0;
    
    for(let i = 0; i < nums.length; i++){
        sum += nums[i];
        
        if(sum > minSum){
            countOfSubarrays++;
            sum = nums[i];
        }
    }
    
    if(countOfSubarrays > m){
        return false;
    }
    
    return true;
}


// Actual Logic
const splitArray = (nums, m) => {
    let start = Math.max(...nums);
    let end = nums.reduce((a,b) => a + b);
    let result = -1;
    
    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));
        if(isValidScheme(nums,mid,m)){
            result = mid;
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    
    return result;
};

