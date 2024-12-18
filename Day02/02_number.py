# 숫자 타입 int, float, complex
age = 7
print(age, "의 타입은 ", type(age))

score = 7.1212
print(score, "의 타입은 ", type(score))

polar_coordinate = 1-2j # +-를 띄워쓰지 않도록 주의
print(polar_coordinate, "의 타입은 ", type(polar_coordinate))


age = int(7)
score = float(29.33)
polar_coordinate = complex(1,-2)
print(type(age), type(score), type(polar_coordinate))

# 함수를 통한 데이터 변환
age =  int(7.0)
score = float( 88 )
polar_coordinate = complex(age)
print(age, score, polar_coordinate)

# 함수를 통한 데이터 변환(글자 -> 숫자)
age = int ("3484")
print ( age, type(age))