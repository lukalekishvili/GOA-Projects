
function func(n){
    if (n>0){
        console.log(n)
        func(n-1)
    } 
}
console.log(func(5))