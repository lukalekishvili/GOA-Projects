# codewars

# link: https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python

# code:
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if mpg * fuel_left >= distance_to_pump:
#         return True
#     elif distance_to_pump < (mpg * fuel_left):
#         return True
#     else:
#         return False  

# codewars

# link:https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/python

# code:
# def rps(p1, p2):
#     if p1 == p2:
#         return "Draw!"
#     elif p1 == "scissors" and p2 == "paper":
#         return "Player 1 won!"
#     elif p1 == "paper" and p2 == "rock":
#         return "Player 1 won!"
#     elif p1 == "rock" and p2 == "scissors":
#         return "Player 1 won!"
#     else:
#         return "Player 2 won!"

# codewars

# link:https://www.codewars.com/kata/544a54fd18b8e06d240005c0

# code:
# def find_smallest(numbers, to_return):
#     smallest_value = min(numbers)
#     if to_return == "value":
#         return smallest_value
#     elif to_return == "index":
#         return numbers.index(smallest_value)

# codewars

# link:https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/python

# code:
# def calc(x):
#     total = ''
#     for i in x:
#         total += str(ord(i))
#     total2 = total.replace('7', '1')
#     sum_total = 0
#     for digit in total:
#         sum_total += int(digit)
#     sum_total2 = 0
#     for digit in total2:
#         sum_total2 += int(digit)

#     return sum_total - sum_total2

# codewars

# link:https://www.codewars.com/kata/565f5825379664a26b00007c/train/python

# code:
# def get_size(w, h, d):
#     return [2 * (w*h + h*d + w*d), w*h*d]