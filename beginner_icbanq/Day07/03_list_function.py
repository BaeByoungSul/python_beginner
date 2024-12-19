user = ['Spencer', 7,  202.2]

user.append( 10000)
print(user)
# user +=[20000,]
# print(user)

# 삽입
user = ['Spencer', 7,  202.2]
user.insert(2, 10000)
print(user)

#index , count

score1 = [35,50,70]
score2 = [15,20,40]
total_score = score1 + score2 
print(total_score)

score1.extend(score2)
print(score1)

score1.reverse()
print(score1)
