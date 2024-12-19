import time

# print(time.localtime())
# print(time.localtime().tm_year)

# print('Stop 1s')
# time.sleep(1)
# print('Go')


# 시간차이 

print(time.time())  # from 1970.01.01 00:00 to now 까지의 초

start = time.time()
time.sleep(1)
end = time.time()

print(end-start)