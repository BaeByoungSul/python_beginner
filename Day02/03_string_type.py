name = "Spencer"
lang = "Python"
profile_comment = """안녕하세요. 스펜스입니다.
저는 파이썬에 관심이 있습니다.
"""

print(name, "의 타입은 ", type(name))
print(lang, "의 타입은 ", type(lang))
print(profile_comment, "의 타입은 ", type(profile_comment))

# 함수를 통한 데이터 변환
birth_year = 1968
birth_month = 5
print( birth_year+birth_month)

birth_year = str(birth_year)
birth_month = str(birth_month)
print( birth_year+birth_month)

# index, value
greeting_message = "Healo Python! Hello!"
print(greeting_message[0])
print(greeting_message[1])
print(greeting_message[-1])
print(greeting_message[-3])

# slice, slicing
print(greeting_message[0:1])
print(greeting_message[0:2])
print(greeting_message[2:5])
print(greeting_message[2:])

# Step을 줄 수도 있다.[start, end, step]
text ="1234567890"
print(text[::3])
print(text[1::3])
print(text[2::3])