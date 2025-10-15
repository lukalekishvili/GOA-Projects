/*
codewars 

link:https://www.codewars.com/kata/57b9fc5b8f5813384a000aa3/train/javascript

code:
function calculate(str) {

  let words = str.split(" ");
  let a=undefined
  let b=undefined 
  let op=undefined;

  for (let i = 0; i < words.length; i++) {
    if (!isNaN(words[i])) {
      if (a === undefined) a = Number(words[i]);
      else b = Number(words[i]);
    }
    if (words[i] === "loses" || words[i] === "gains") op = words[i];
  }

  if (op === "loses") return a - b;
  if (op === "gains") return a + b;

}











*/