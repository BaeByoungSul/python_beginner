# 현재 working Dir
import os 
os.chdir(os.path.dirname(__file__))

load_data = [
  ("학생1", 100), ("학생2", 90), ("학생3", 70),
]

# 템플릿
message = """{}님 안녕하십니까.
담당자 스펜스입니다.
국가시험 000의 결과를 안내해드립니다
감사합니다.
점수 : {}
"""
for name, score in load_data:
  print(name, score)
  filename = '{} 결과값.txt'.format(name)
  # print(filename)

  new_message = message.format(name, score)
  with open(filename, 'w', encoding='utf-8') as fp2 :
    fp2.write(new_message)