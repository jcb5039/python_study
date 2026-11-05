# 12장 문제 1 정답
#
# 해설 (문제 읽는 순서대로):
# 2. 손으로: M = 80 → 40/80*100 = 50, 80/80*100 = 100, 60/80*100 = 75 → 평균 (50+100+75)/3 = 75
# 4. 방법: 최댓값 M을 한 번 구한다 → 각 점수를 바꾼 리스트를 만든다 → 평균
# - max(scores)는 반복문 밖에서 한 번만 구해요. (컴프리헨션 안에 넣으면 매번 다시 구해요)
#
# 다른 풀이 (수학으로 줄이기):
#   새 평균 = (모든 점수의 합 / M * 100) / N
#   print(f'{sum(scores) / m * 100 / n:.2f}')

n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
new_scores = [s / m * 100 for s in scores]
print(f'{sum(new_scores) / n:.2f}')
