/*
callback არის ფუნქციაში შექმნილი ფუნქცია
მაგალითად:                 */
function hello(){
    return function greet(){
        console.log("hello")
    }
}
hello()()
