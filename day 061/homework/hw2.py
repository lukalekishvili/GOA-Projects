import random
nums=[1,2,3,4,5,6,7,8,9,10]
guessnums = random.choice(nums)
usernum = int(input('entrer random number from 1 to 10: '))
if usernum != guessnums:
    print("you couldn't guess the num")
else:
    print("you guess the number")
