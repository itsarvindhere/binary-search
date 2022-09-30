//Given an array of length ‘N’, where each element denotes the position of a stall. Now you have ‘N’ stalls and an integer ‘K’ which denotes the number of cows that are aggressive. To prevent the cows from hurting each other, you need to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. Return the largest minimum distance.

/*


    e.g. stalls = [1,2,4,8,9] and k = 3

    Imagine we place c1 at stall 1, c2 at stall 2 and c3 at stall 4

    Distance between c1 and c2 = 1
    Distance between c2 and c3 = 2


    Minimum Distance  = 1

    -----------------------
    If we place c1 at stall 1, c2 at stall 4 and c3 at stall 9
    
    Distance between c1 and c2 = 3
    Distance between c2 and c3 = 5

    Minimum Distance = 3

    -----------------------

    If we place c1 at stall 1, c2 at stall 8 and c3 at stall 9
    
    Distance between c1 and c2 = 7
    Distance between c2 and c3 = 1

    Minimum Distance = 1

    -----------------------

    If we place c1 at stall 2, c2 at stall 4 and c3 at stall 9
    
    Distance between c1 and c2 = 2
    Distance between c2 and c3 = 5

    Minimum Distance = 2

    -----------------------

    If we place c1 at stall 1, c2 at stall 4 and c3 at stall 8
    
    Distance between c1 and c2 = 3
    Distance between c2 and c3 = 4

    Minimum Distance = 3


    So far minimum distances = [3,1,3,1,2,3]

    Largest minimum distance  = 3 <- ANSWER!!

    --------------------------------------------------

    Lets think of a solution. Can we have 1 as answer? Yes we can because if we place cow1 at stall 1 and cow2 at stall 2 then distance between these two is 1. Even if we keep cow3 at stall 4 and the distance between cow2 and cow3 is 2, the minimum distance is 1.

    So 1 can be a valid minimum distance between two cows. 

    Can we have 2 has a valid minimum distance? YES. 

    What if we place cow1 at stall2 and cow3 at stall 4 and cow 3 at stall 8

    In that case minimum distance will be 2 only. 

    and so on ......

    If we try to see if minimuim distance is 4 then can we place 3 cows 

    we place cow1 at stall 1
    can we place cow2 at stall 2 ? NO! because in that case distance between cow1 and cow2 will be (2-1) = 1. But we want minimum distance to be 4

    can we place cow2 at stall 4 ? NO! because in that case distance between cow1 and cow2 will be (4-1) = 3. But we want minimum distance to be 4

    can we place cow2 at stall 8 ? YES! because in that case distance between cow1 and cow2 will be (8-1) = 7 which is >= minimum distance of 4.

    But now, we cannot place cow3 at 9th stall becaue distance between cow3 and cow2 = 9 - 8 = 1 which is not >= min distance

    Hence, if minimum distance is 4, we cannot place 3 cows in the stalls.

    Hence the final answer is 3 only because above 3, the minmimum distance will not work.

    So this is monotonic function.

    Anwswer is possible at 1, 2, 3
    Answer is not possible at 4

    And since answer is not possible at 4, it is not possible at any number above 4. Whether it is 5,6,7,8,....

    So this is a monotonic function.

    BINARY SEARCH CAN BE APPLIED HERE!

    Search space will start from 1 -> start = 1

    But what about the end??

    the worst case can be if we have two cows and we place each at far ends of the array. 

    e.g. in above array, c1 at stall 1 and c2 at stall 9

    So in that case, distance will be 8. Hence worst case can be the difference between first and last.

    start = 1.
    end = 8.

*/

// Helper method to check if a minimum distance is valid or not
const isValid = (stalls, minDistance, cows) => {
    let countOfCows = 1;
    let prevPosition = stalls[0];

    for(let i = 1; i < stalls.length; i++){
        if(stalls[i] - prevPosition >= minDistance) {
            countOfCows++;
            prevPosition = stalls[i];
        }

        if(countOfCows === cows) return true;
    }

    return false;
}

//Main Logic
const aggressiveCows = (stalls, cows) => {

    stalls.sort((a,b) => a - b);

    let start = 1;
    let end = stalls[stalls.length - 1] - stalls[0];
    let result = -1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));

        if(isValid(stalls, mid, cows)){
            result = mid;
            // If this is valid then we need to look at numbers higher than mid because we want to maximize the minimum distance between cows.
            start = mid + 1;
        } else{
            //if mid distance is not valid that means any value above mid will also not be valid so we need to look at  values lesser than mid
            end = mid - 1;
        }
    }

    return result;

}


let stalls = [1,2,4,8,9];
let cows = 3;

console.log("Largest minimum distance between cows is:", aggressiveCows(stalls,cows));
