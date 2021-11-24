;(function () {
    return console.log('f1');
    
})();

// higher Order

function Highe(fn){
    fn();
}

Highe(function(){console.log('hi')});

function high2(){
    return function(){
        console.log('function2');
    }
}
var x = high2()
x();

function some(){
    console.log(this)
}