# 9장 문제 2 정답
#
# 해설:
# - is_even: n % 2 == 0 자체가 True/False라서 그대로 돌려주면 돼요.
#     if n % 2 == 0:
#         return True
#     return False
#   이렇게 써도 맞지만, 한 줄이 더 깔끔해요.
# - grade: return을 만나면 함수가 끝나니까, 위에서 걸리면 아래 if는 검사하지 않아요.
#   그래서 elif/else 없이 if만 이어 써도 돼요. 마지막 줄은 어떤 if에도 안 걸린 경우예요.
# - can_ride: 조건식을 바로 돌려줘요.


def is_even(n):
    return n % 2 == 0


def grade(score):
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'


def can_ride(age, height):
    return age >= 12 and height >= 140


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
