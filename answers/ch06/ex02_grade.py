# 6장 문제 2 정답
#
# 해설:
# - 높은 점수 조건부터 위에 써요. 위에서 걸리면 아래는 검사하지 않으니까
#   elif score >= 80 만 써도 "80 이상 90 미만"이라는 뜻이 돼요.
#
# 자주 틀리는 점:
# - score >= 60 을 맨 위에 쓰면 95점도 D가 나와요.
# - 90점(경계값)에서 B가 나오면 > 와 >= 를 헷갈린 거예요.

score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
