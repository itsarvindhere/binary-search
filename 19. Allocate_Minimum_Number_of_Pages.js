
//Check if a particular scheme of distribution of pages is valid or not between k students
//We have to check if we can distribute all the books between k students with this scheme
// We have a maxPages variable and we have to allocate books between k students such that all students are allocated all the books in array and also a student cannot get pages above maxPages

const isValidScheme = (arr,maxPages,k) => {
    let countOfStudents = 1; //Start with at least one student
    let pages = 0;

    for(let i = 0; i < arr.length; i++){
        pages += arr[i];
        if(pages > maxPages) {
            countOfStudents++;
            pages = arr[i];
        }
    }
    if(countOfStudents > k){
        return false;
    }

    return true;
}


// Logic for minimizing the number of pages
const minimumPages = (arr, k) => {
    
    // If number of books to allocate is less than number of students then we cannot allocate at least one book to each student
    if(arr.length < k) return -1;


    let start = Math.max(...arr);
    let end = arr.reduce((a,b) => a + b);
    let result = -1;

    while(start <= end){
        let mid = Math.trunc(start + ((end - start)/2));
        if(isValidScheme(arr,mid,k)){
            result = mid;
            end = mid - 1;
        } else{
            start = mid + 1;
        }
    }


    return result;
}



let arr = [12,34,67,90];
let k = 2;


console.log("Minimum Number of pages:", minimumPages(arr,k));