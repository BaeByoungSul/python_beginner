# list type
user = ['Spencer', 7, 202.2, 10000]
print(user, type(user))

# indexing 
print(user[0])
print(user[1])
print(user[-1])

# slicing
print(user[0:2])
print(user[0:-2])

# del 명령어
del user[3]
print(user)

# str -> list
greeting_str = "hello bbs"
greeting_list = list(greeting_str)

print(greeting_str, greeting_list)
