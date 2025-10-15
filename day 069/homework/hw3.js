let counter = {
    num: 0,
    add(){
        this.num++
        return this
    },
    remove(){
        this.num--
        return this
    },
    show(){
        console.log(this.num)
        return this
    }
}

counter.add().add().add().remove().show()