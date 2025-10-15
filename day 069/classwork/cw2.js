let car = {
    brand: "Mercedes-Benz",
    speed: 0,
    drive: function(){
        this.speed = 50
        console.log("Car is driving at " + this.speed + " km/h")
    },
    stop:function(){
        this.speed = 0
        console.log("car stoped")
    }
}

car.drive()