// 1
const greet = name => 'hello ' + name

console.log(greet("luka"))

// 2
const math = (a, b) => {
    return a + b
}

console.log(math(10,5))

// 3
let name = prompt("enter your name: ")
let age = Number(prompt("enter your age: "))
const final = (name, age) => {
    if(age < 18){
        return `sorry ${name} but you need to be at least 18 to enter` 
    }else{
        return `welcome ${name}`
    }
    
}

console.log(final(name,age))