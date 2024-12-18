import random

# print(random.random())
# print(random.randint(0,255))
# print(random.uniform(0,255))

# num_1_45 = range(1,46)
# print(list(num_1_45), type(num_1_45))

# num_6_45 = random.sample(range(1,46), 6)
# print(num_6_45)

# 
numbers = [1,2,3,4,5,6,7,8,9]
random.shuffle(numbers)
print(numbers)