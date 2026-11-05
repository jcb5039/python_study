# 7장 문제 6 정답
#
# 해설:
# - n % 10 으로 일의 자리를 꺼내 더하고, n //= 10 으로 일의 자리를 지워요.
# - 한 번 지울 때마다 자릿수(digits)를 1 늘려요.
# - n이 0이 되면 모든 자리를 다 쓴 거라 반복이 끝나요.
#
# 다른 풀이 (문자열로):
#   s = input()
#   total = 0
#   for ch in s:
#       total += int(ch)
#   print(len(s))
#   print(total)
#   → 숫자를 글자로 보고 한 글자씩 도는 방법. 코테에서는 이쪽도 많이 써요.

n = int(input())
digits = 0
total = 0
while n > 0:
    total += n % 10
    n //= 10
    digits += 1
print(digits)
print(total)
