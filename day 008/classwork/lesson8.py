#1
reversed_string = input("shemoiyvanet sityva an winadadeba: ")
res = " "
for i in reversed_string:
    res = i + res

print(res)

#2
sum = 0 
for i in range(101):
    sum += i

print(sum)

#3

user_input = input("put in a 3 letter word ")

if len(user_input) != 3:
        print("sheiyvane 3 asoiani sityva")
else:
    is_palindrome = True
    for i in range(len(user_input) // 2):
        if user_input[i] != user_input[-(i + 1)]:
            is_palindrome = False
    print(is_palindrome)

#4
for i in range(100,301):
    print(i**2)
    
#5
for i in range(1000):
    if i % 2 == 0:
        print(False)
    else:
        print(True)

#bonus
int1 = int(input("shemoiyvanet raime ricxvi: "))
int2 = int1 ** 0.5

print(int2) 
                                     
