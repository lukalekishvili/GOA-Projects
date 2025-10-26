const p = document.getElementsByClassName("p1")

const colors = ["red", "blue", "green", "orange", "purple"]

for(let i = 0; i < p.length; i++) {
    p[i].style.backgroundColor = colors[i]
}

