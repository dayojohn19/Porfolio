function say(message){
    return this.name + ' is '+ message;
}

var p4 = {name:'john'};
z = say.apply(p4,['awesome']);

console.log(z)