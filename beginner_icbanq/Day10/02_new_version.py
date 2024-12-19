# f-string 3.6
age =  4
print("I'm {:02d} years old".format(age))
print(f"I'm {age:02d} years old")

# list comprehension
result = []
for i in range(1,10):
  result.append(i*2)
print(result)

result2 = [i*2 for i in range(1,10)]
print(result2)