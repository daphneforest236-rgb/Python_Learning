#程序之间共享数据
# import json
# numbers = [2,3,5,7,11,13]

# filename = 'number.json'
# with open(filename, 'w') as f:
#     json.dump(numbers,f)

# import json
# filename = 'number.json'
# with open(filename) as f:
#     number = json.load(f)
# print(number)

# # 存储用户的名字
# import json
# username = input("What's is your name?")
# filename = 'username.json'
# with open(filename, 'w') as f:
#     json.dump(username,f)
#     print("We'll remember you when you come back, " + username + "!")

# #向用户发出问候
# import json
# filename = 'username.json'

# with open(filename) as f:
#     username = json.load(f)
#     print("Welcome back, " + username + "!")

#将这两个程序合并到一个程序
# import json
# filename = 'username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name?")
#     with open(filename,'w') as f:
#         json.dump(username,f)
#         print("We'll remember you when you come back, " + username + "!")
# else:
#     print("Welcome back, " + username + "!")

#重构
# import json
# def greet_user():
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name?")
#         with open(filename,'w') as f:
#             json.dump(username,f)
#             print("We'll remember you when you come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")

# greet_user()

# import json
# def get_stored_username():
#     """如果存储了用户名，就获取它"""
#     filename = 'username.json'
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#          return None
#     else:
#          return username
# def greet_user():
#     """问候用户，并指出其名字"""
#     username = get_stored_username()
#     if username:
#         print("Welcome back, " + username + "!") 
#     else:
#         username = input("What is your name?")
#         filename = 'username.json'
#         with open(filename,'w') as f:
#             json.dump(username,f)
#             print("We'll remember you when you come back, " + username + "!")
# greet_user()

