import time

# print(time.localtime())
# print(time.localtime().tm_year)

# print('Stop 1s')
# time.sleep(1)
# print('Go')

# print(time.time())

start = time.time()
time.sleep(1)
end = time.time()

print(end-start)