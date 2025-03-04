#1
num = int(input("enter a number: "))
for i in range(1,num + 1):
    if num % i == 0:
        print(i)

#2
# While Loop არის ფუნქცია რომელიც აგრძელებს რაიმის ამოპრინტვას იქამდე სანამ ის არის True
#მაგალითად:

# name = input("enter your name: ")
# while name == "":
#     print("you did not enter name")
# else:
#   print("hello {name}")

#ან

# name = input("enter your name: ")
# while name == "":
#     print("you did not enter name")
#     name = input("enter your name: ")
# else:
#     print("hello {name}")

#ამ შემთხვევაში "you did not enter your name" და "enter your name: "  Terminal-ში ამოიპრინტება უსასრულოდ


#for loop არის ფუნქცია რომელსაც ვუთითებთ რამდენჯერ შეასრულოს დავალება, რა რიცხვიდან რიცხვამდე შექმნას დიაპაზონი
#და რამდენი ნაბიჯი გადადგას შესრულების დროს, ასევე შეგვიძლია For ციკლით გადავუაროთ ლისტებს სადაც ჩვენი ინდექსი შეეხება ყველა ელემენტს

#4
#(1 and 0) or (1 and 1) and (0 or 0) ეს გამოსახულება გამოიტანს False-ს რადგან
#ჯერ სრულდება and შემდეგ or ამიტომ პირველი შესრულდება (1 and 1) and (0 or 0) და შემდეგ მიღებული პასუხი შეედრება (1 and 0) ამას
#და მივიღებთ False-ს

