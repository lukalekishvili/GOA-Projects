# num = 15,22,31,43,55,66,74,568,977,710
# res = []
# for i in num:
#     if i%2==0:
#         res.append(i)
# print(res)



# nums = [1,5,2,14,76,88,98,91,11,253]
# res =[]
# def isPrime(n):
#     if n == 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# for i in nums:
#     if isPrime(i):
#         res.append(i)
# print(res)


# def CW1(L,num):
#     res = []
#     for i in L:
#         if i % num == 0:
#             res.append(i)
#     return res
# 
# print(CW1([1,23,165,2,3,92,10,34,911],3))




# listt = [1, 2, 3, 4, 5]

# listt.clear()
# print(listt)

# listt = [1, 2, 3, 4, 5]

# listtt = listt.copy()
# print(listtt)


# listt = [1, 2, 3, 4, 5]

# print(listt.count(2))

# listt = [1, 2, 3, 4, 5]

# print(listt.index(2))


# listt = [1, 2, 3, 4, 5,]

# listt.remove(1)

# print(listt)

# listt = [5,4,3,2,1]
# listt.sort()
# print(listt)

# listt = [1, 2, 3, 4, 5]

# listt.reverse()

# print(listt)


# listt = [1, 2, 3, 4, 5]
# def manual_len(L):
#     res = 0
#     if type(L) == list:
#         for i in L:
#             res += 1
#     elif type(L) == str or type(L) == int:
#         for i in str(L):
#             res += 1
        
#     return res






# list1 = [1, 7, 3, 23]
# list2 = [4, 7, 9, 5]

# list3 = []
# for item in list1:
#     list3.append(item)
# for item in list2:
#     list3.append(item)










# lst=[0,0,0,0,0,0,1,0,1]
# sum=0
# for i in lst:
#     if i == 1:
#         sum+=i
# print(sum)


sett=('word', 'hello','bye')
sett= hash('hello')
print(sett)