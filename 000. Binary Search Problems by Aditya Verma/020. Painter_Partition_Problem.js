/*
    We have to paint n boards of length {A1, A2…An}. There are k painters available and each takes 1 unit of time to paint 1 unit of the board. 
    
    The problem is to find the minimum time to get this job done if all painters start together, under the constraints that any painter will only paint continuous sections of boards.

    e.g. arr = [5,10,30,20,15] and painters = 3

    So, we have 3 painters and there are five boards. Since we have to assign the boards to paint 'continuously', we cannot assign board 1 and then board 4 to some painter. The assignment needs to be in a continuous fashion only.

    Since each painter takes 1 unit time to paint 1 unit of a board, that means, the array basically gives us the time that each painter will take for a board. e.g., 5 units time for 5 unit length board and so on...

    The job can be done in minimum time if one particular painter does not have a lot of work to do and the others have minimum to no work. We have to distribute the work evenly between them.

    This is a variation of the "Allocate Minimum Pages" problem. Because in that problem as well, we have some books that we want to allocate between students and we want to ensure that the stress is minimum on each student. 

    In allocate pages problem, we started from the maximum number of pages in array because we know that a student needs to have at least one book allocated to him. So that time, we allocated the book with max pages to the student. 

    Here as well, since we want to find the least amount of the time in which the painters can finish painting the boards, that time would obviously be greater or equal to the maximum length in the array. 

    e.g. arr = [10,20,30,15];

    Here, max length is 30 which means this board will take 30 units of time to paint. Hence, the minimum time taken to paint all the boards is going to be greater or equal to 30 only. It cannot be any value below 30. e.g. we cannot say that 20 is the minimum time because that does not make sense when we have a board of length 30, taking 30 units of time. 
    
    
    Hence our binary search starts from 30 till the sum of all lengths (75 in above case).

*/


// Helper Method to check if a particular unit of time can be the solution
const isValidScheme = (arr, maxTime, painters) => {
    let count = 1;
    let time = 0;

    for(let i = 0; i < arr.length; i++){
        time += arr[i];
        if(time > maxTime) {
            count++;
            time = arr[i];
        }
    }

    if(count > painters){
        return false;
    }

    return true;
}


// Actual Logic
const minimumTimeTakenToPaint = (arr, painters) => {
    let start = Math.max(...arr); 
    let end = arr.reduce((a,b) => a + b);
    let result = -1;

    while(start <= end) {
        let mid = Math.trunc(start + ((end - start)/2));
        if(isValidScheme(arr,mid,painters)) {
            result = mid;
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }

    return result;

}


let arr = [10,5,20,25,17,23,2,9,4,13];
let painters = 7;

console.log("Minimum Time will be:", minimumTimeTakenToPaint(arr,painters))
