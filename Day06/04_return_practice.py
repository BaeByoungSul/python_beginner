def count_number_state(n_list):
  state = {
    'positive' : 0,
    'negative' : 0,
    'zero':0
  }
  # 음수가 몇개인지 
  for n in (n_list):
    if n > 0:
      state['positive'] +=1
    elif n < 0:
      state['negative'] +=1
    else:
      state['zero'] +=1
    
  return state

# 함수 실행
n_list = [-3, -2, -1, 0, 1,2,3,4,]
result =  count_number_state( n_list)
print( result )
#print("{}의 음수 개수는 {}개다".format(n_list, result))