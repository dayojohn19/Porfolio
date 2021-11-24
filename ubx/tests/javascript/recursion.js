arr = [1,3,4,2];
function moveup(a,b){
    for (i=a; i <= b;i++){
        console.log(i);
        arr.push(i)
    };
}


// moveup(1,5)

arr.reduce(moveup)

console.log(arr)