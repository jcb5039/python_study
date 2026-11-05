# 12장 문제 5 정답
#
# 해설: 10장(개수 세기) + 11장(정렬 기준 두 개) + 12장(빠른 입력)을 합친 문제예요.
# 1. sys.stdin.readline으로 빠르게 읽고, 이름은 .rstrip()으로 줄바꿈을 지워요.
#    rstrip()을 빼먹으면 'kim\n'처럼 줄바꿈이 붙은 이름이 저장돼서 출력이 한 줄씩 밀려요.
# 2. 딕셔너리로 이름별 표수를 세요.
# 3. votes.items()는 (이름, 표수) 짝들 → 표수 내림차순(-v[1]), 같으면 이름 오름차순(v[0])
# 4. 정렬된 순서대로 출력해요.
#
# 시간: 세기 N번 + 정렬 (후보 수가 적으면 아주 빠름). 10만 줄도 금방 끝나요.

import sys
input = sys.stdin.readline

n = int(input())
votes = {}
for _ in range(n):
    name = input().rstrip()
    votes[name] = votes.get(name, 0) + 1

ranking = sorted(votes.items(), key=lambda v: (-v[1], v[0]))
for name, count in ranking:
    print(name, count)
