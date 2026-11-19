# 3장 문제 3: 짝수 판별과 자릿수 꺼내기
#
# 할 일: (1)~(5)의 None을 지우고, n으로 계산하는 식을 쓰세요.
# 규칙: 8처럼 답을 직접 쓰면 안 돼요. n이 다른 수로 바뀌어도 맞는 값이 나오는 식이어야 해요.
# (답: …)은 식을 계산했을 때 변수에 들어가야 하는 값이에요. 답을 그대로 쓰면 안 돼요.
#
# 채점: python3 exercises/ch03/ex03_digits.py
# 힌트: 강의 3장 "몫과 나머지는 이런 데 써요" → 짝수/홀수, 일의 자리 꺼내기

n = 4728

# (1) n이 짝수인지를 비교식으로 쓰세요. 식의 결과(True나 False)가 변수에 담겨요.
#     비교 연산자 == 를 쓰세요. (답: True)
is_even = n % 2 == 0

# (2) n에서 일의 자리 숫자를 꺼내는 식을 쓰세요. (답: 8)
ones = 4728 % 10

# (3) n에서 마지막 두 자리를 꺼내는 식을 쓰세요. (답: 28)
last_two = 4728 % 100

# (4) n에서 천의 자리 숫자를 꺼내는 식을 쓰세요. (답: 4)
thousands = n // 1000

# (5) n에서 십의 자리 숫자를 꺼내는 식을 쓰세요. (답: 2)
#     도전! 몫과 나머지를 둘 다 써야 해요.
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
