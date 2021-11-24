x = 10;
i = 0;
arr = [];
while (i <= x){
    i++;
    if (i % 3 || i % 5 == 0) {
        arr.push(i);
        // console.log(i)
    };
    console.log('*'.repeat(i))
    

}
console.log(arr.reduce((a,b)=> {return a+b}))