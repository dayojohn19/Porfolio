var obj = {
    name:'vv',
    surname:'yy',
    getName: function(){
        console.log(this.name)
    },
    getSur: function(){
        console.log(this.surname)
    }
}


obj.getSur();
obj.getName();