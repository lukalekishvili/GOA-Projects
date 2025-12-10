const arr = [10, 20, 30, 40]

arr.forEach((item, index) => {
    arr[index] = item + 5
})
console.log(arr) 
