
# 현재 working Dir
import os 
os.chdir(os.path.dirname(__file__))

# 파일 읽기 : read(), readline(), readlines()
# fp1 = open('02.txt', 'rt', encoding='utf-8')
# print(fp1.read() )
# fp1.close()

with open('04.txt', 'r', encoding='utf-8') as fp2 :
  print(repr(fp2.readline()))
  print('{!r}'.format(fp2.readline()))
  print('{!r}'.format(fp2.readline()))
  
with open('04.txt', 'r', encoding='utf-8') as fp2 :
  print(repr(fp2.readlines()))

