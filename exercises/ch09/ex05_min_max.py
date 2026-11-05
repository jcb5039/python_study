# 9장 문제 5: 값 두 개 돌려주기
#
# 채점: python3 exercises/ch09/ex05_min_max.py
# 힌트: 강의 9장 "값 여러 개 돌려주기"


# (1) 리스트를 받아서 (가장 작은 값, 가장 큰 값)을 돌려주세요. min(), max()는 써도 돼요.
#     min_max([3, 1, 2]) → (1, 3)
def min_max(nums):
    pass  # TODO


# (2) 초(seconds)를 받아서 (분, 초)를 돌려주세요.
#     split_time(375) → (6, 15)
def split_time(seconds):
    pass  # TODO


# (3) 문자열을 받아서 (대문자 개수, 소문자 개수)를 돌려주세요. 다른 글자는 세지 않아요.
#     count_case('Hello World') → (2, 8)
#     힌트: 글자 ch가 대문자인지는 ch.isupper(), 소문자인지는 ch.islower() 로 알 수 있어요.
#           (4장의 isdigit()과 같은 종류의 메서드예요)
def count_case(s):
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

check(min_max, ([3, 1, 2],), (1, 3))
check(min_max, ([5],), (5, 5))
check(split_time, (375,), (6, 15))
check(split_time, (59,), (0, 59))
check(count_case, ('Hello World',), (2, 8))
check(count_case, ('ABC def 123',), (3, 3))
check(count_case, ('',), (0, 0))
