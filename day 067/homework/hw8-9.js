let prods = [
{
    name: "iPhone 17 pro max",
    price: 5000
},
{
    name: "iPad",
    price: 4599
},
{
    name: "MacBook Pro",
    price: 6999
},
{
    name: "Airpods Pro 2",
    price: 900
},
{
    name: "iPhone 3g case",
    price: 10
},
]
let expensiveitem = prods[0]
for(let exp of prods){
    if (exp.price > expensiveitem.price){
        expensiveitem = exp
    }
}

console.log(expensiveitem)

for(names of prods){
    console.log(names.name)
}