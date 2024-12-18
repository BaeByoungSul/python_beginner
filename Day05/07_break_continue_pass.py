# pass  아무것도 안함
for i in range(1,10):
  if i % 3 == 0: 
    pass

for i in range(1,10):
  if i % 3 == 0: 
    continue
  print(i)

print ('-'*8)
for i in range(1,10):
  if i % 3 == 0: 
    break
  print(i)