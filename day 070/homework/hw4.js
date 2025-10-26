const custh = document.getElementsByClassName("h11")

const colors = ["red", "blue", "green", "purple"];


for (let i =0; i < custh.length; i++){
    custh[i].style.backgroundColor = colors[i];
    custh[i].style.border = "3px solid black";
    custh[i].style.borderRadius = "15px";
}