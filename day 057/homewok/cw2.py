fruits = []
for i in range(5):
    fruit = input(f"ჩაწერე შენი {i+1}-ე საყვარელი ხილი: ")
    fruits.append(fruit)
fruits.append("grape")   
fruits.append("dragon fruit")
fruits.pop()
print(sorted(fruits))