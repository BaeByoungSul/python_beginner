# format을 통해 변수 값을 문자열에 넣기
student = "배병술"
school = "아이씨뱅큐"
principal = "스펜서"

# 기본 사용 방법
text = "{}{}{}".format(student, school, principal)
print( text )
text = text.format(student, school, principal)
print( text )


print("=" * 20)
students = ["배병술", "이정우", "낙동강", "정상택"]

for student in students:
  print("안녕하십니까 {} 학부모님 저는 {} 교장 {}입니다.".format(student, school, principal))