let arr = [10,30,21,59.99,122.59,100]

arr = arr.map(price => price * 0.8).reduce((acc,price)=> acc + price,0)

console.log(arr)