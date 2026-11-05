# 8장 문제 2 정답
#
# 해설:
# - 평균 = sum / len
# - 평균보다 높은 사람 수: 리스트를 돌면서 조건에 맞을 때만 count += 1
# - 출력할 때만 :.2f 로 자르고, 비교할 때는 원래 평균(average)을 써요.
#   반올림한 값으로 비교하면 경계에서 틀릴 수 있어요.
#
# 자주 틀리는 점:
# - "높은"인데 >= 를 써서 평균과 같은 사람(70점)까지 셈

n = int(input())
scores = list(map(int, input().split()))
average = sum(scores) / len(scores)

count = 0
for s in scores:
    if s > average:
        count += 1

print(f'{average:.2f}')
print(count)
