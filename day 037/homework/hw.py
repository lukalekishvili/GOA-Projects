# codewars

# link:https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

# code:
# def accum(st):
#     index = 1
#     result = []
#     for i in st:
#         i = i * index
#         i = i.capitalize()
#         index += 1
#         result.append(i)
#     return '-'.join(result)

# codewars

# link:https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

# code:
# def descending_order(num):
#     string = str(num)
#     sorted_list=sorted(string, reverse=True)
#     joined_list = ''.join(sorted_list)
#     final_num = int(joined_list)
#     return final_num

# codewars

# link:https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

# code:
# def is_square(n):
#     return n >= 0 and (n**0.5) % 1 ==0

# codewars

# link:https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

# code:
# def is_solved(board):
#     for row in board:
#         if row[0] == row[1] == row[2] != 0:
#             return row[0]
#     for col in range(3):
#         if board[0][col] == board[1][col] == board[2][col] != 0:
#             return board[0][col]
#     if board[0][0] == board[1][1] == board[2][2] != 0:
#         return board[0][0]
#     if board[0][2] == board[1][1] == board[2][0] != 0:
#         return board[0][2]
#     for row in board:
#         for cell in row:
#             if cell == 0:
#                 return -1
#     return 0

# codewars

# link:https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

# code:
# def find_next_square(sq):
#     i = 1 
#     sqq = sq
#     while sqq > 0:
#         sqq -= i 
#         i += 2
#     if sqq == 0:
#         return sq + i
#     else:
#         return -1


