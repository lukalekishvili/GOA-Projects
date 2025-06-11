# 1

# def split(strn):
#     wrd = ''
#     res = []
#     for i in strn:
#         if i == ' ':
#             res.append(wrd)
#             wrd = ''
#         else:
#             wrd+=i
#     if wrd: 
#         res.append(wrd)
#     return res

# print(split('dato lika lela darbaza'))

# codewars 1

# link: https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python

# code:def sum_str(a, b):
#     if a == '' and b == '':
#         return '0'
#     elif a == '':
#         return b
#     elif b == '':
#         return a
#     else:
#         return str(int(a) + int(b))

# codewars 2

# link: https://www.codewars.com/kata/55a5bfaa756cfede78000026/train/python

# code: def problem(a):
#     if type(a) == str:
#         return "Error"
#     else:
#         res = a * 50
#         res+=6
#     return res

# codewars 3

# link:

# code:

# codewars 4

# link: https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

# code: def delete_nth(lst, n):
#     result = []
#     seen = {}

#     for num in lst:
#         if num not in seen:
#             seen[num] = 1
#             result.append(num)
#         elif seen[num] < n:
#             seen[num] += 1
#             result.append(num)

#     return result