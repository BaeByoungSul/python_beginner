# list 예시
texts = ['가','나','다','라','마']

for text in texts:
  print(text)

# 중첩리스트
users = [
  [1, 'bbs'], [2, 'lbs'], [3, 'ddd']
]
print(users)

numbers = [3, 5, 7, 9, 12]
circles = []
for r in numbers:
  circles.append(r * r * 3.14)
  
print(circles)
