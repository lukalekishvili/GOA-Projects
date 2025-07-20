# codewars

# link:https://www.codewars.com/kata/56b1eb19247c01493a000065/train/python

# code:
# def unique_sum(lst):
#     if lst == []:
#         return None
#     samenum = []
#     total = 0
#     for i in lst:
#         if i not in samenum:
#             samenum.append(i)
#             total += i
#     return total

# codewars

# link:https://www.codewars.com/kata/5a145ab08ba9148dd6000094/train/python

# code:
# def doubles(s):
#     stack = []
#     for char in s:
#         if stack and stack[-1] == char:
#             stack.pop()
#         else:
#             stack.append(char)
#     return ''.join(stack)