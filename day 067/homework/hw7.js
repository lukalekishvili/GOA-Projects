let cars = [
{
    brand: "Mercedes-benz",
    year: 2005
},
{
    brand: "BMW",
    year: 2017
},
{
    brand: "TOYOTA",
    year: 2025
},
{
    brand: "DODGE",
    year: 2025
}
]

for (let car of cars){
    if (car.year > 2023){
        console.log(car.brand)
    }
}
