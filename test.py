name = input("saxeli: ")
amount = 0
for i in name:
    if i == "A":
        print(i)
        amount = amount + 1

# if amount == 0:
#     print("theres no A's in your name")


# num = int(input("please input a number: "))
# result = 1 
# for i in range(1,num+1):
#         result *= i    #result = result * i

# print(result)


# s = input("word pls: ")
# res = " "
# for i in s:
#     res = i + res

# print(res)


# num = int(input("enter a number: "))

# count = 0
# while num == 1:
#     num = int(input("invalid number, try again: "))
# for i in range(2,num):
#     if num % i == 0 and count == 0:
#         print("your number is not a prime")
#         count += 1
# if count == 0:
#     print("your number is a prime")



# print("the password has to be over 8 letters, must contain an upper character and must have a number")

# password = input("please input a password: ")
# while len(password) < 8 or "A" not in password:
#     password = input("please try again: ")
# print("correct")

# num = int(input("please input a number: ")) #6
# count = 0
# while num==1:
#     num=int(input("try another number: "))
# for i in range(2,num):
#     if num % i == 0 and count == 0:
#         print('Your number is not a prime')
#         count += 1
# if count == 0:
#     print('your number is a prime')