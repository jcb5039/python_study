# 8장 문제 3 정답
#
# 해설:
# - 첫 줄은 숫자 두 개 → a, b = map(...) 모양
# - 둘째 줄은 숫자 N개 → list(map(...)) 모양
# - 빈 리스트(result)를 만들고, 조건에 맞는 것만 append
# - print(*result)로 '1 4 2 3' 모양으로 출력
#
# 다른 풀이 (리스트에 담지 않고 바로 출력):
#   for x in nums:
#       if x < limit:
#           print(x, end=' ')
#   → 맨 끝에 띄어쓰기가 하나 더 붙지만, 대부분의 채점(이 judge.py도)은 줄 끝 공백을 무시해요.

n, limit = map(int, input().split())
nums = list(map(int, input().split()))

result = []
for x in nums:
    if x < limit:
        result.append(x)

print(*result)
