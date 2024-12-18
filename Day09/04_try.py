try:
  n1 = int ('3')
  n2 = int ('3.0')
  
except TypeError:
  print( "Type오류")
except ValueError:
  print( "Value 오류")
except:
  print("111111")
finally:
  print('finally')
