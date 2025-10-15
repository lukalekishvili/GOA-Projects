 
let calculator = {
    user1: Number(prompt("enter first number: ")),
    user2: Number(prompt("enter second number: ")),
    user3: prompt("enter a sumbol: +, -, /, "),
    calc(){
        if (this.user3 == "+"){
            return this.user1 + this.user2
        }
        else if (this.user3 == "-"){
            return this.user1 - this.user2
        }
        else if (this.user3 == "/"){
            return this.user1 / this.user2
        }
        else if (this.user3 == ""){
            return this.user1 - this.user2
        }
    }
}
console.log(calculator.calc())