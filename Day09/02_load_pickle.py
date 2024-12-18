import pickle, os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

# 가져오기
with open('school_data.pickle', 'rb') as fp:
  load_data = pickle.load(fp)

print(load_data)