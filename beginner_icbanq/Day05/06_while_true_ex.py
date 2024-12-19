user_input = input('0을 입력할 때까지 ')

basket=[]
while True:
  if user_input =="0": 
    break

  basket.append(user_input)
  user_input = input('0을 입력할 때까지 ')

print("최종: {}".format(basket))