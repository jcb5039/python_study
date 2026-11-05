# 3장 문제 3: 짝수 판별과 자릿수 꺼내기
#
# None 자리에 계산식을 쓰세요. 숫자를 직접 쓰지 말고 n으로 계산하세요.
#
# 채점: python3 exercises/ch03/ex03_digits.py
# 힌트: 강의 3장 "몫과 나머지는 이런 데 써요" → 짝수/홀수, 일의 자리 꺼내기

n = 4728

# (1) n이 짝수인지 True/False로 담으세요. (비교 연산자 == 를 쓰세요)
is_even = None

# (2) 일의 자리 숫자 → 8
ones = None

# (3) 마지막 두 자리 → 28
last_two = None

# (4) 천의 자리 숫자 → 4
thousands = None

# (5) 십의 자리 숫자 → 2   (도전! 몫과 나머지를 둘 다 써야 해요)
tens = None

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
