user_dict = {
  'name': 'bbs',
  'age': 55,
  'height': 174,
  'salary': 200

}

# key, value, item
print(list(user_dict.keys()))
print(list(user_dict.values()))
print(list(user_dict.items()))

# items() 
for k,v in user_dict.items():
  print(k, v)