def count_negative(n_list):
  # 음수가 몇개인지 
  count = 0
  for n in (n_list):
    if n < 0: count += 1
  return count

# 함수 실행
n_list = [-3, -2, -1, 0, 1,2,3,4,]
result =  count_negative( n_list)
print("{}의 음수 개수는 {}개다".format(n_list, result))