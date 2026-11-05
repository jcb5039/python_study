# 11장 문제 1: 리스트 컴프리헨션
#
# 모든 함수를 리스트 컴프리헨션 한 줄(return [ ... ])로 써 보세요.
#
# 채점: python3 exercises/ch11/ex01_comprehension.py
# 힌트: 강의 11장 "리스트 컴프리헨션", "조건 붙이기"


# (1) 1부터 n까지 각 수의 제곱을 담은 리스트
#     squares(4) → [1, 4, 9, 16]
def squares(n):
    pass  # TODO


# (2) 리스트에서 양수(0보다 큰 수)만 담은 리스트
#     only_positive([3, -1, 0, 5]) → [3, 5]
def only_positive(nums):
    pass  # TODO


# (3) 단어 리스트에서 각 단어의 첫 글자만 담은 리스트
#     first_letters(['apple', 'banana']) → ['a', 'b']
def first_letters(words):
    pass  # TODO


# (4) 길이가 3 이상인 단어만, 대문자로 바꿔서 담은 리스트
#     long_upper(['hi', 'cat', 'python']) → ['CAT', 'PYTHON']
def long_upper(words):
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

check(squares, (4,), [1, 4, 9, 16])
check(squares, (1,), [1])
check(only_positive, ([3, -1, 0, 5],), [3, 5])
check(only_positive, ([-2, -1],), [])
check(first_letters, (['apple', 'banana'],), ['a', 'b'])
check(long_upper, (['hi', 'cat', 'python'],), ['CAT', 'PYTHON'])
check(long_upper, ([],), [])
