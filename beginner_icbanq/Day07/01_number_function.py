n1, n2 = 3, 3.5

print(n1, float(n1))
print(n2, int(n2))

# 소수점 연산 -> 부동 소수점 연산
print( 1.1 + 2.2 )
print( 1.1 + 2.7 )
print( 1.1 + 2.6 )

# 부동 소수점 연산 문제를 해결 :  decimal 사용
from decimal import Decimal
print( Decimal(1.1) + Decimal(2.2) )
print( Decimal('1.1') + Decimal('2.2') )
# print( 1.1 + 2.7 )
# print( 1.1 + 2.6 )

