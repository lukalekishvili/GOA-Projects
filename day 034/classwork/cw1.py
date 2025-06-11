# codewars 1

# link: https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/python

# code: def validate_hello(greetings):
#         greetings = greetings.lower()
#         return (
#         'hello' in greetings or
#         'ciao' in greetings or
#         'salut' in greetings or
#         'hallo' in greetings or
#         'hola' in greetings or
#         'ahoj' in greetings or
#         'czesc' in greetings)

# codewars 2

# link: https://www.codewars.com/kata/57037ed25a7263ac35000c80/train/python

# code:
# from urllib.parse import quote

# def generate_link(username):
#     result = ""
#     for char in username:
#         if char == "/":
#             result += "/"
#         else:
#             result += quote(char)
#     return "http://www.codewars.com/users/" + result
