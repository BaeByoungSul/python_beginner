# list type
user = ['Spencer', 7, 202.2, 10000]
print(user, type(user))
user_dict= {'name':'Spencer', 'age': 7, 'height': 202.2, 'salary': 10003}
# print(user_dict, '의 타입은', type(user_dict) )

# print(user_dict)
# keying 
print(user_dict['name'])
print(user_dict['age'])

user_dict['salary'] += 1000

print(user_dict['salary'])