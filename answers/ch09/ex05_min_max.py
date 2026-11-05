# 9장 문제 5 정답
#
# 해설:
# - return a, b 처럼 쉼표로 나눠 쓰면 두 값이 묶여서(튜플) 돌아가요.
#   받는 쪽에서는 low, high = min_max(...) 처럼 나눠 받을 수 있어요.
# - count_case: 개수를 두 개 세니까 변수도 두 개(upper, lower) 준비해요.
#   isupper()/islower()는 숫자나 띄어쓰기에서는 False라서 저절로 빠져요.


def min_max(nums):
    return min(nums), max(nums)


def split_time(seconds):
    return seconds // 60, seconds % 60


def count_case(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower


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

check(min_max, ([3, 1, 2],), (1, 3))
check(min_max, ([5],), (5, 5))
check(split_time, (375,), (6, 15))
check(split_time, (59,), (0, 59))
check(count_case, ('Hello World',), (2, 8))
check(count_case, ('ABC def 123',), (3, 3))
check(count_case, ('',), (0, 0))
