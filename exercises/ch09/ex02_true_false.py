# 9장 문제 2: 참거짓과 학점을 돌려주는 함수
#
# 채점: python3 exercises/ch09/ex02_true_false.py
# 힌트: 강의 9장 "return을 만나면 함수는 바로 끝나요" + 6장 조건문


# (1) n이 짝수면 True, 아니면 False를 돌려주세요.
#     is_even(4) → True
#     도전: if 없이 한 줄로도 쓸 수 있어요. (비교식의 결과가 이미 True/False니까요)
def is_even(n):
    pass  # TODO


# (2) 점수를 받아 학점 문자열을 돌려주세요. (6장 문제 2와 같은 기준)
#     90 이상 'A', 80 이상 'B', 70 이상 'C', 60 이상 'D', 나머지 'F'
#     grade(85) → 'B'
#     도전: elif와 else를 쓰지 말고 if와 return만으로 써 보세요.
def grade(score):
    pass  # TODO


# (3) 나이(age)와 키(height)를 받아서, 12살 이상이고 키가 140 이상이면 True를 돌려주세요.
#     can_ride(12, 140) → True
def can_ride(age, height):
    pass  # TODO


# ───── 채점 코드 ─────
# 9장까지 배웠다면 이제 읽을 수 있어요! (try/except는 에러가 나도 멈추지 않게 하는 문법이에요)

def check(func, args, expected):
    call = f"{func.__name__}({', '.join(repr(a) for a in args)})"
    try:
        actual = func(*args)
    except Exception as e:
        print(f'❌ {call}  에러: {type(e).__name__}: {e}')
        return
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {call}')
    else:
        print(f'❌ {call}  결과: {actual!r}  기대: {expected!r}')

check(is_even, (4,), True)
check(is_even, (7,), False)
check(is_even, (0,), True)
check(grade, (85,), 'B')
check(grade, (90,), 'A')
check(grade, (59,), 'F')
check(grade, (60,), 'D')
check(grade, (100,), 'A')
check(can_ride, (12, 140), True)
check(can_ride, (11, 150), False)
check(can_ride, (20, 139), False)
