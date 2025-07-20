# codewars

# link:https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

# code:
# def get_count(sentence):
#     res = 0
#     for i in sentence:
#         if i in 'aeiou':
#             res +=1
#     return res

# codewars

# link:https://www.codewars.com/kata/57f36495c0bb25ecf50000e7/train/python

# code:
# def find(n):
#     res = 0
#     for i in range(n+1):
#         if i % 3 == 0 or i % 5 == 0:
#             res += i
#     return res
# codewars

# link:https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

# code:
# def get_middle(s):
#         if len(s) % 2 == 0:
#             return s[len(s)//2 - 1:len(s)//2+1]
#         else:
#             return s[len(s)//2]
            
# codewars

# link:https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python

# code:
# def count_by(x, n):
#     lst = []
#     for i in range(x,x*n+1,x):
#         lst.append(i)
#     return lst
# codewars

# link:https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

# code:
# def filter_list(l):
#     lst=[]
#     for i in l:
#         if type(i) != str:
#             lst.append(i)
#     return lst

# codewars

# link:https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

# code:
# def descending_order(num):
#     lst = []
#     for i in str(num):
#         lst.append(int(i))
#     lst.sort()
#     lst.reverse()
#     res = ''
#     for i in lst:
#         res = res + str(i)
#     return int(res)
# codewars

# link:https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

# code:
# def square_digits(num):
#     res = ''
#     for i in str(num):
#         res = res + str(int(i)**2)
#     return int(res)
