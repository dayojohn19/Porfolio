arr1 = ['a ba ka ',1,2,3,'kjl'];
ns = [];

function ItsNumber(n){
    // i = n == 2 ? 'wee':i;
    ns.push(n);
    console.log('arr1: ',n)
}

function ItsString(s){
    vowels = /a|e|i|o|u/gi;
    if (s.match(vowels)){
        console.log(s,'has vowels');
    } else {
        console.log(s, 'No Vowels');
    }
    
}

for (i in arr1){
    n = arr1[i]
    typeof(n) === 'number' ? ItsNumber(n) : ItsString(n);
}

// -----------------
console.log(ns)
console.log('\n \n getting max....');
max = Math.max(...ns);
console.log('max: ',max);
