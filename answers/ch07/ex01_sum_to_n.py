# 7장 문제 1 정답
#
# 해설:
# - total을 반복문 밖에서 0으로 시작하고, 1부터 N까지 하나씩 더해요.
# - 1부터 N까지는 range(1, n + 1). range(n)은 0부터 n-1까지라서 N이 빠져요.
#
# 다른 풀이:
# - print(sum(range(1, n + 1)))  ← sum은 8장에서 배워요.
# - print(n * (n + 1) // 2)      ← 수학 공식. 반복 없이 바로 계산해요.

n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print(total)
