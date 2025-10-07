students = {
    "Ana": 95,
    "Giorgi": 88,
    "Luka": 76
}
for name, score in students.items():
    if score >=90:
        print(name, score)
students.update({"Nino": 100})
print(students)