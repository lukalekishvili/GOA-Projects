# 1
# x = 10
# if isinstance(x, bool):
#     print("Science")
# elif isinstance(x, (int, float)):
#     print("Math")
# elif isinstance(x, str):
#     print("Literature")
# else:
#     print("Unknown type")


# 2

# def func(listt):
#     final_num=0
#     strr=0
#     intt=0
#     floatt=0
#     booleann=0
#     for i in listt:
#         if isinstance(i, bool):
#             booleann+=1
#         elif isinstance(i,str):
#             strr +=1
#         elif isinstance(i,int):
#             intt+= 1
#         else:
#             floatt+=1
#     final_listt=[strr,intt,floatt,booleann]
#     final_listt=sorted(final_listt)
#     return final_listt[-1]
# print(func(['strr','intt',11,1,1,2,5,True]))


# 3

# def func(x):
#     res =[]
#     for i in x:
#         if isinstance(i,int):
#             res.append(i)
#     return res
# print(func([1,2,3,122,'11']))

# 4

# def func(x):
#     return type(x)
# print(func(10))