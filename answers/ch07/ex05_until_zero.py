# 7장 문제 5 정답
#
# 해설:
# - 몇 줄일지 모르니까 for 대신 while True + break 를 써요.
# - 읽자마자 0인지 먼저 검사하고, 0이면 더하기 전에 break 해요.
# - 합계(total)와 개수(even_count)를 반복문 밖에서 0으로 시작해요.
#
# 다른 풀이 (while 조건에 바로 쓰기):
#   n = int(input())
#   while n != 0:
#       ... (계산)
#       n = int(input())

total = 0
even_count = 0
while True:
    n = int(input())
    if n == 0:
        break
    total += n
    if n % 2 == 0:
        even_count += 1
print(total)
print(even_count)
