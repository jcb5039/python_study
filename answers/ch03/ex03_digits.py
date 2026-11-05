# 3장 문제 3 정답
#
# 해설:
# - is_even: 2로 나눈 나머지가 0이면 짝수 → n % 2 == 0
#   (% 가 == 보다 먼저 계산돼요: 4728 % 2 → 0, 0 == 0 → True)
# - ones: 10으로 나눈 나머지 → 8
# - last_two: 100으로 나눈 나머지 → 28
# - thousands: 1000으로 나눈 몫 → 4
# - tens: 10으로 나눈 몫(472)에서 다시 일의 자리 꺼내기 → 472 % 10 → 2
#   이렇게 "// 10 으로 한 자리씩 지우고, % 10 으로 꺼내는" 방법은
#   7장 반복문에서 각 자리 숫자의 합 같은 문제를 풀 때 또 써요.

n = 4728

is_even = n % 2 == 0
ones = n % 10
last_two = n % 100
thousands = n // 1000
tens = n // 10 % 10

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('is_even', is_even, True)
check('ones', ones, 8)
check('last_two', last_two, 28)
check('thousands', thousands, 4)
check('tens', tens, 2)
