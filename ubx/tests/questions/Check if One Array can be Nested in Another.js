
// Create a function that returns true if the first array can be nested inside the second.

arr1 = [1,2,3]
arr2 = [4,5,6]

function same(arr1,arr2){

for (i in arr2){
    console.log(i);
        if (
            arr1.find(element=> element ==arr2[i])
        ) {
            console.log('found');
            return false
        }
    }
    return true
}

console.log(same(arr1,arr2));