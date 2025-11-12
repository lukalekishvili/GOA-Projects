// 1
const func1 = (cb) => {
    console.log("hello,")
    cb()
}

const func2 = () => {
    console.log("bye.")
}

func1(func2)

// 2
const funqcia1 = (callback) => {callback(),callback(),callback()}
const test = () => {console.log("hello")}
funqcia1(test)

// 3
const f1 = (callback) => {callback()}
f1(function(){console.log("hello")})

