# 셋 타입: 중복이 없는 데이터 관리구조
number_list = [1,2,3,4,5,5]
number_set  = {1,2,3,4,4,5}

print(number_list, number_set)

# 리스트, 튜플, 문자열 -> 셋
basket_list = ['사과', '바나나', '사과', '코코넛', '바나나']
basket_set = set(basket_list)
print(basket_set)

text="djklasdfjldsaf"
print(set(text))