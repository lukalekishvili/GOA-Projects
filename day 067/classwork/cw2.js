let dihtionary1 = {
    name: "luka",
    id: 1,
    grade: 67
}
let dihtionary2 = {
    name: "lasha",
    id: 2,
    grade: 41
}
function compare(dihtionary1,dihtionary2){
    if (dihtionary1.grade < dihtionary2.grade){
        return dihtionary2.name;
    }else if (dihtionary1.grade > dihtionary2.grade){
        return dihtionary1.name
    }else {
        if (dihtionary1.id > dihtionary2.id){
            return dihtionary1.name
        } else if (dihtionary1.id < dihtionary2.id){
            return dihtionary2.name
        }else{
            return "none" 
        }
    }
}