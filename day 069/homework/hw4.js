let message = {
    word: "",
    addword(){
        this.word += "dihtionary"
        return this
    },
    upper(){
        this.word = this.word.toUpperCase()
        return this
    },
    show(){
        console.log(this.word)
        return this
    }
}

message.addword().upper().addword().show()