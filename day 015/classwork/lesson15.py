# 1

# def CW1(L,num):
#     res = []
#     for i in L:
#         if i % num == 0:
#             res.append(i)
#     return res

# print(CW1([1,23,165,2,3,92,10,34,911],3))

# 2

# https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python


# def reverse_list(l):
#     lis = []
#     for i in range(len(l)-1,-1,-1):
#         lis.append(l[i])
#     return lis

# 3

# https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python


# def even_last(numbers):
#     res = 0
#     if len(numbers) == 0:
#         return 0
#     for i in range(0,len(numbers),2):
#         res += numbers[i]
#     return res * numbers[-1]