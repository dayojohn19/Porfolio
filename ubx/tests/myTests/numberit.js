// n = 0;
// for (i=0; i<=1000; i++){
//     if (i % 5 == 0 || i % 3 == 0 ){
//         console.log(n+=i);
//     }
// }

// while (i!=10){
//     i++;
//     console.log(i);
// }
n=0
function checkit(i){
    i % 5 == 0 || i % 3 == 0 ? n += i : console.log('not',n)
}
setTimeout(
   ()=>{ 
       i=0;
        do {
            i++;
            console.log(i)
            checkit(i);
        }
        while(i!= 10);
        console.log('n is: ',n) ;
    }   
    ,
    2000)
