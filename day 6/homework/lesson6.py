#1
num = int(input("random num: "))
count = 0
for i in range(1,num + 1,2):
    count += i

print(count)


#2
num2 = int(input("input a number: "))
for i in range(1,num2+1):
    if num2 % i == 0:
        print(i)
    
#3
password = input("Password: ")
count = 3
while password != "Goa123":
    print("password incorrect")
    password = input("Try again: ")
    count -= 1
    print("you have " + str(count) + " tries left")
    if count == 0:
        print("your account has been blocked, contact support to unblock it")
        break
    else:
        print("Password is correct")

# print("the password has to be over 8 letters, must contain an upper character and must have a number")
# count = 3
# password = input("please input a password: ")
# while len(password) < 8 or "A" not in password:
#     password = input("please try again: ")
#     count -= 1
#     if count == 0:
#         print("agar gaq cdebi")
#         break
#     else:
#         print("you have skibidi password")

#4
sityva = input("chaweret raime sityva: ")
res = ""
for i in sityva:
    res = i + res
print(res) 


    
    
                                            