import pickle, os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

# 가져오기
try:
  with open('school_data.pickle', 'rb') as fp:
    load_data = pickle.load(fp)
except:
  print('loading failed')    
  load_data = []
finally:
  print('finally')
print(load_data)