x = [];


for (i = 0; i!= 20; i++){
    if (i % 5 == 0){
        x.push(i);
    }
};
console.log('raw: ', x);

c='';
for (i=0;i!=x.length;i++){
    c += (x[i]);
}
console.log('added: ',c);


// join
z = x.join();
console.log('join : ',z);
// map
y = x.map((a)=>{return a*2});
console.log('mapped: ', y);
// reduce
x = x.reduce((a,b)=>{return a+b});
console.log('reduced sum: ', x);
