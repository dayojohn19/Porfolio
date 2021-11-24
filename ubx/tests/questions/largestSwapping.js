// Write a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.

function swapit(num){
    n = num.toString().split('');
    x = n[0]>=n.pop() ? true : false;

    return x
}

console.log(swapit(233));
console.log(swapit(322));
console.log(swapit(324));
console.log(swapit(423));

