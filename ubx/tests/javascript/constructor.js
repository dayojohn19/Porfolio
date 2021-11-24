function p(name,age){
    this.name = name;
    this.age  = age;
}

p1 = new p('jc',24);
p2 = new p('cj', 3);

console.log(p1,p2.age)