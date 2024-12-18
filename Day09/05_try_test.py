aget = -1
attemp = 0 

while attemp < 5 :
  attemp += 1
  try: 
    age = int(input("나이"))
  except:
    print (attemp)
    
print('Exit')    