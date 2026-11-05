# 7장 문제 4 정답
#
# 해설:
# - 첫 줄의 N만큼 반복하면서 매번 input()으로 한 줄씩 읽어요.
# - 번호가 1부터 필요하니까 range(1, n + 1)로 돌고 i를 번호로 써요.
#
# 자주 틀리는 점:
# - range(n)으로 돌면서 i를 그대로 쓰면 Case #0 부터 나와요. (i + 1 로 써도 돼요)
# - 'Case #1:' 의 콜론 뒤 띄어쓰기

n = int(input())
for i in range(1, n + 1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a + b}')
