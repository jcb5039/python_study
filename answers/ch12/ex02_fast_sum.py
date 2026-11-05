# 12장 문제 2 정답
#
# 해설:
# - import sys / input = sys.stdin.readline 두 줄만 위에 추가하면, 나머지는 7장과 똑같아요.
# - 숫자로 바꿀 때는 int()가 줄바꿈을 알아서 무시해서 rstrip()이 필요 없어요.
#
# 더 빠르게 (출력도 많을 때):
#   print를 10만 번 하는 것도 시간이 걸려요. 결과를 리스트에 모아 한 번에 출력할 수 있어요.
#   result = []
#   for _ in range(n):
#       a, b = map(int, input().split())
#       result.append(str(a + b))
#   print('\n'.join(result))
#   ('\n'은 줄바꿈 문자예요. 줄바꿈을 사이에 넣어서 합치는 거예요)

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)
