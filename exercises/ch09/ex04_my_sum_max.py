# 9장 문제 4: sum과 max 직접 만들기
#
# 파이썬에 있는 sum(), max()를 쓰지 말고, 반복문으로 직접 만들어 보세요.
#
# 채점: python3 exercises/ch09/ex04_my_sum_max.py
# 힌트: 강의 7장 "패턴 1: 합계 구하기", "패턴 3: 가장 큰 값 찾기"
#       음수만 있는 리스트도 있어요! 최댓값은 0이 아니라 첫 번째 값으로 시작하세요.


# (1) 리스트의 합을 돌려주세요. 빈 리스트면 0이에요.
#     my_sum([1, 2, 3]) → 6
def my_sum(nums):
    pass  # TODO


# (2) 리스트에서 가장 큰 값을 돌려주세요. 리스트는 비어 있지 않아요.
#     my_max([3, 9, 2]) → 9
def my_max(nums):
    pass  # TODO


# (3) 리스트의 평균을 돌려주세요. 위에서 만든 my_sum을 써 보세요.
#     my_average([1, 2, 3, 4]) → 2.5
def my_average(nums):
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

check(my_sum, ([1, 2, 3],), 6)
check(my_sum, ([],), 0)
check(my_sum, ([-5, 5, 10],), 10)
check(my_max, ([3, 9, 2],), 9)
check(my_max, ([7],), 7)
check(my_max, ([-5, -2, -9],), -2)
check(my_average, ([1, 2, 3, 4],), 2.5)
check(my_average, ([10, 20],), 15.0)
