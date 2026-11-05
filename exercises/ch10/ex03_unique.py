# 10장 문제 3: 중복 제거
#
# 채점: python3 exercises/ch10/ex03_unique.py
# 힌트: 강의 10장 "중복 제거하기"


# (1) 리스트에 서로 다른 값이 몇 개 있는지 돌려주세요.
#     count_unique([5, 3, 5, 1, 3]) → 3
def count_unique(nums):
    pass  # TODO


# (2) 중복을 없애고 작은 수부터 정렬한 리스트를 돌려주세요.
#     unique_sorted([5, 3, 5, 1, 3]) → [1, 3, 5]
def unique_sorted(nums):
    pass  # TODO


# (3) 두 리스트에 모두 들어 있는 값만, 작은 수부터 정렬한 리스트로 돌려주세요.
#     common([1, 2, 3, 4], [3, 4, 5]) → [3, 4]
def common(a, b):
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

check(count_unique, ([5, 3, 5, 1, 3],), 3)
check(count_unique, ([7, 7, 7],), 1)
check(count_unique, ([],), 0)
check(unique_sorted, ([5, 3, 5, 1, 3],), [1, 3, 5])
check(unique_sorted, ([2, 2],), [2])
check(common, ([1, 2, 3, 4], [3, 4, 5]), [3, 4])
check(common, ([1, 1, 2], [2, 2, 9]), [2])
check(common, ([1, 2], [3, 4]), [])
