text = """안녕하세요
멀티라인 텍스트 입니다.
파이선 파일 처리를 배우고 있어요
"""

# 파일객체 생성
# 파일이 깨짐 : File >> Preferences >> Setting >> Text Editor >> 
#              Files >> Auto Guess encoding 체크
with open('./Day08/01.txt', 'a') as  fp:
  fp.write(text)

import time
while True:
  time.sleep(1)