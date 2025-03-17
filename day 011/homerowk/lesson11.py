#1
#https://www.codewars.com/kata/5810085c533d69f4980001cf/train/python

# def calculator(a, b, operator):
#     if type(a) in (int, float) and type(b) in (int, float):
#         if operator == '+':
#             return a + b
#         if operator == '-':
#             return a - b
#         if operator == '*':
#             return a * b
#         if operator == '/':
#             return a / b if b != 0 else "unknown value"
#     return "unknown value"

#2https://www.codewars.com/kata/57e1e61ba396b3727c000251/train/python

# def string_clean(s):
#     res = ''
#     for i in s:
#         if not i.isdigit():
#             res += i
#     return res

#3

#https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python

# def add_length(str_):
#     splitted = str_.split()
#     res = []
#     for i in splitted:
#         lenned = ''
#         lenned += i
#         lenned += ' '
#         lenned += str(len(i))
#         res.append(lenned)
#     return res


#4
#https://www.codewars.com/kata/55f1b763dd670651620000ce/train/python

# def count_char_occurrences(strng, char):
#     count = 0
#     for i in strng:
#         if char == i:
#             count += 1
#     return count