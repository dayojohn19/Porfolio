var num = [
    001110,
    10001,
    11111,
    10001,
    10001,
];


p=0;
while (p != num.length){

    var digits = num[p].toString().split('');
    x = [];
    for (i=0;   i != digits.length; i++){
        if (digits[i] == 0) {
            y = ' '
        }else {
            y = '*'
        }
        
        x.push(y)
    };
    console.log('x: '+ x.join(''));
    p++;
}





for (ii=0; ii<= 1; ii++){


}





// digits.map((x)=>{

//     console.log('* '.repeat(x))
// });

