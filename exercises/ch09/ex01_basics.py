# 9장 문제 1: 간단한 함수 세 개
#
# 각 함수의 pass  # TODO 줄을 지우고 몸통을 채우세요.
# 결과는 print가 아니라 return으로 돌려줘야 해요!
#
# 채점: python3 exercises/ch09/ex01_basics.py
# 힌트: 강의 9장 "return: 결과 돌려주기"


# (1) 두 수 a, b를 받아서 합을 돌려주세요.
#     add(3, 5) → 8
def add(a, b):
    pass  # TODO


# (2) 수 n을 받아서 제곱(n * n)을 돌려주세요.
#     square(4) → 16
def square(n):
    pass  # TODO


# (3) 이름을 받아서 '안녕, 이름!' 문자열을 돌려주세요.
#     greet('민지') → '안녕, 민지!'
def greet(name):
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

check(add, (3, 5), 8)
check(add, (-1, 1), 0)
check(square, (4,), 16)
check(square, (-3,), 9)
check(greet, ('민지',), '안녕, 민지!')
check(greet, ('Python',), '안녕, Python!')
