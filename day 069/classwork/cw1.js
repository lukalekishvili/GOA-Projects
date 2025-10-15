let greeet = {
    name: "luka",
    greet: function(){
        console.log("hello " + this.name)
    },
}

greeet.greet()