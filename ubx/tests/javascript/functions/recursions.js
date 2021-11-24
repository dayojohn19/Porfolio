function creator(name, made){
    this.name = name,
    this.made = made
    this.wallet = 10
    this.add = (val) => {
        return val+this.wallet
    }   
}

x = new creator('jj', 'aa');
console.log(x.add(1));