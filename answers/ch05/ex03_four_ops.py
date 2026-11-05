# 5장 문제 3 정답
#
# 해설:
# - 몫은 //, 나머지는 % 예요.
# - print를 다섯 번 쓰면 다섯 줄로 나와요.
#
# 자주 틀리는 점:
# - 몫을 A / B 로 쓰면 2.3333333333333335 처럼 실수가 나와요.

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
