//1  
const text = document.getElementById("id1").textContent = "Hello world"
//2
const text2 = document.getElementsByClassName("class1")[0]
text2.style.backgroundColor = "red"
text2.style.fontSize = "100px"
//3
const h11 = document.querySelector("h1").innerText = "gamarjoba samyaro"
//4
const p = document.getElementsByClassName("p1")
for (let i = 0; i < p.length; i++) {
  p[i].style.backgroundColor = "lightblue";
  p[i].style.margin = "5px";
  p[i].style.padding = "10px";
  p[i].style.borderRadius = "8px";
}
