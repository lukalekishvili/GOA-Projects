let people = [
{
    name: "lasha",
    age: 17
},
{
    name: "luka",
    age: 67
},
{
    name: "andria",
    age: 1
},
{
    name: "Giorgi",
    age: 18
}
]
console.log(people)

for (let unc of people){
    if(unc.age >= 18){
        console.log(unc.name)
    }

}

