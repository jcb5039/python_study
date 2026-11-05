# 6장 문제 3 정답
#
# 해설 (방법 1, 아래 코드):
# - a가 b와 c 둘 다보다 크거나 같으면 a가 가장 커요.
# - 아니면 b가 c보다 크거나 같으면 b, 아니면 c.
# - >= 를 써야 같은 수가 있을 때도 빠짐없이 걸려요. > 만 쓰면 5 5 3 에서 아무것도 안 걸리는
#   조건이 생길 수 있어요.
#
# 방법 2 (7장 이후 자주 쓰는 방식): "지금까지 가장 큰 수"를 변수에 두고 하나씩 비교해요.
#   biggest = a
#   if b > biggest:
#       biggest = b
#   if c > biggest:
#       biggest = c
#   print(biggest)
#
# 실제 코테에서는 print(max(a, b, c)) 한 줄이면 돼요. 원리를 알고 쓰는 게 중요해요.

a, b, c = map(int, input().split())
if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)
