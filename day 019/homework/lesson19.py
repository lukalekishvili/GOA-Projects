# 1

# list1 = [8,9,4,66,45,7]
# list2 =[3,5,6,89,5,2,3,]
# def func(l, ll):
#     lll = l+ll
#     lll.sort()
#     return lll
# print(func(list1, list2))

# 2
# lista = [1, 4, 7]
# listb = [2, 2, 2, 10]
# def func(l1, l2):
#     sum1 = sum(l1)
#     sum2 = sum(l2)
#     if sum1 > sum2:
#         return l1
#     else:
#         return l2
# res = func(lista, listb)
# print(res)

# 3
# list_a = [1, -4, -7, 33, -9]
# list_b = [21, 24, 2, -10]
# def func(l1,l2):
#     count1=0
#     count2=0
#     for i in l1:
#         if i < 0:
#             count1+=1
#         elif i>0:
#             count2+=i

#     for i in l2:
#         if i >0:
#             count2+=i
#         elif i <0:
#             count2+=1
#     return [count1, count2]
# res=func(list_a, list_b)
# print(res)

# 4
# list_a = [1, 4, 7, 6, 2, 3, 10, 9]
# def func(l):
#     li =[]
#     for i in l:
#         if i %3 != 0:
#             li.append(i)
#     return li
# res=(func(list_a))
# print(res)

# 5

# list_a = [1, 4, 7]
# def func(l):
#     li=[]
#     for i in l:
#         li.append(i*2)
#     return li
# res=func(list_a)
# print(res)