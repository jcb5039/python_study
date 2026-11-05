# 6장 문제 4 정답
#
# 해설:
# - 규칙을 "윤년인 경우"로 정리하면 두 가지예요.
#   (1) 4의 배수이면서 100의 배수가 아닐 때   → year % 4 == 0 and year % 100 != 0
#   (2) 400의 배수일 때                        → year % 400 == 0
#   둘 중 하나라도 맞으면 윤년 → or 로 합쳐요.
# - and 가 or 보다 먼저 계산되지만, 헷갈리지 않게 괄호를 쳤어요.
#
# 다른 풀이 (elif로 위에서부터 걸러내기):
#   if year % 400 == 0:
#       print(1)
#   elif year % 100 == 0:
#       print(0)
#   elif year % 4 == 0:
#       print(1)
#   else:
#       print(0)
#   → 가장 까다로운 조건(400)을 맨 위에 둔 게 포인트예요.

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)
