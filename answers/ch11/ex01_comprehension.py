# 11장 문제 1 정답
#
# 해설: 모두 [담을 것 for 변수 in 꺼낼 곳 if 조건] 모양이에요.
# - squares: 1부터 n까지 → range(1, n + 1), 담을 것은 x * x
# - only_positive: if x > 0 으로 거르기
# - first_letters: 담을 것이 w[0]
# - long_upper: 거르는 조건(len(w) >= 3)과 담을 것(w.upper())이 둘 다 있어요.
#
# for문으로 쓰면 (long_upper):
#   result = []
#   for w in words:
#       if len(w) >= 3:
#           result.append(w.upper())
#   return result


def squares(n):
    return [x * x for x in range(1, n + 1)]


def only_positive(nums):
    return [x for x in nums if x > 0]


def first_letters(words):
    return [w[0] for w in words]


def long_upper(words):
    return [w.upper() for w in words if len(w) >= 3]


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
