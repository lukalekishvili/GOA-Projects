let arr = [
    {name:"luka",age:16},
    {name:"nika",age:15},
    {name:"lasha",age:19},
    {name:"dato",age:67}
]

arr = arr.filter(el => el.age>=18).map(el=>el.name)

console.log(arr)