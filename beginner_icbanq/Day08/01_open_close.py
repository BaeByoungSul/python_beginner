text = """안녕하세요
멀티라인 텍스트 입니다.
파이선 파일 처리를 배우고 있어요
"""

# 파일객체 생성
# 파일이 깨짐 : File >> Preferences >> Setting >> Text Editor >> 
#              Files >> Auto Guess encoding 체크
# fp = open('./Day08/51.txt', 'w')
# fp.write(text)
# fp.close

# 현재 working Dir
import os 
print ('현재의 working Dir ', os.getcwd())

print ( __file__ )
print ( os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))
# print ('현재의 working Dir ', os.getcwd())


fp = open('02.txt', 'w', encoding='utf-8')
fp.write(text)
fp.close