import pickle, os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

# 데이터
class_number = 5 
member = ['스펜스', '낙동강', '청풍명월']
teacher= {
  'name': '귀도',
  'lang': 'Python'
}

# pickle로 저장
save_data = [class_number, member, teacher]
with open('school_data.pickle', 'wb') as fp:
  pickle.dump(save_data, fp)
