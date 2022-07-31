/*
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h hours.

    ------------------------------------------------------

    TO KNOW IF WE CAN USE BINARY SEARCH ON SUCH PROBLEMS, JUST THINK IF THERE IS MONOTONICITY OR NOT.

    If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.

    So in above problem, if lets say k = 4 is a minimum solution, that means, every number above 4 is also correct. ALso, every number below 4 will not be correct. So that is monotonicity. 
    
    In that case, we can use Binary Search to solve this problem.

    WHAT WOULD BE THE START AND END VALUE??

    Since we want to find the minimum eating rate per hour, we know the minimum value can be 1. It cannot be 0 because that makes no sense. Koko can eat at least 1 banana per hour.
    
    So, our start will be 1. 
    
    And our end value will be the max number of bananas in a pile in the given array. Because it is given that in one hour, Koko can only eat bananas in one pile. Even if pile has less than k number of bananas she will not go to the next pile in that hour.

    basically, the ceil is the max number in the array or max number of bananas in a pile because if we take k = max number of bananas in array, that means in one hour, Koko can eat k (max number of bananas in array) bananas so she can finish eating all the bananas in all piles in (length of array) hours.

    And because H will always be >= length of piles array, this will be a correct solution. But, we want a minimum value for k so that will lie between 1 and the max(array).

*/


/* Helper Method to check if a given K value can be a possible solution so that Koko can eat all bananas in <= H hours

e.g. if k = 6 that means Koko can eat 6 bananas in one hour

so if array is [3, 6, 7 , 1]
Then first pile has 3 bananas. So, it can be finished in one hour as the rate of eating is k = 6. 

third pile has 7 bananas so, in one hour, 6 can be eaten off it. Then, in next hour, the one banana left will be eaten. So, pile with 7 bananas takes two hours if k = 6. 

In short, hours taken by a pile = ceil (bananas in pile/k)

AT the end, we just need to check if hours taken to eat all bananas from all piles is less than or equal to the given H or not. If not, then this solution will not work and we need to increase the value of k. i.e., start + 1.

*/
const isValidScheme = (piles, k, h) => {
    let hours = 0;    

    for(let i = 0; i < piles.length; i++){
        hours += Math.ceil(piles[i]/k);
    }

    return hours <= h;
}


// Main Logic
const minEatingSpeed = (piles, h) => {
    let start = 1;
    let end = Math.max(...piles);
    let result = -1;
    
    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));
        if(isValidScheme(piles, mid, h)) {
            result = mid;
            end = mid - 1;
        } else{
            start = mid + 1;
        }
    }
    
    return result;
    
};