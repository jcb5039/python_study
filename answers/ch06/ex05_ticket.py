# 6장 문제 5 정답
#
# 해설:
# - 'Y'는 숫자로 바꿀 수 없으니까 split()으로 나눈 뒤 나이만 int()로 바꿔요.
# - 먼저 나이로 기본 요금을 정하고(price), 그다음 회원 할인을 따로 처리해요.
#   두 단계로 나누면 조건이 훨씬 단순해져요.
# - 무료(0원)는 할인하면 안 되니까 price > 0 일 때만 빼요.
#
# 자주 틀리는 점:
# - age, member = map(int, input().split()) → ValueError ('Y'는 정수가 아님)
# - 65살 이상 회원에게 할인을 적용해서 -1000원이 나옴

age, member = input().split()
age = int(age)

if age <= 7:
    price = 0
elif age <= 13:
    price = 5000
elif age <= 19:
    price = 8000
elif age <= 64:
    price = 12000
else:
    price = 0

if member == 'Y' and price > 0:
    price -= 1000

print(price)
