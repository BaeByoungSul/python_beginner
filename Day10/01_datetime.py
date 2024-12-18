from datetime import datetime, timedelta, timezone

# 현재시간
now = datetime.now()
print( now )

# 독일시간
de_tz = timezone(timedelta(hours=1))
ko_tz = timezone(timedelta(hours=9))

de_now = datetime.now(tz=de_tz)
kr_now = datetime.now(tz=ko_tz)

print(de_tz, kr_now)

# 특정 시간
future = datetime( 2100, 1,1)
print(future)
print(future-now)

# 시간차
period_gap = timedelta( days=1000, hours=2)
finish_day = now + period_gap

print(finish_day, type(finish_day))

# 시간 포맷
# 대소소대대대 
date1 = now.strftime("%Y-%m-%d %H:%M:%S")
print( date1 )
date1 = now.strftime("%Y-%m-%d %p %I:%M:%S %a %b %A %B ")
print( date1 )
