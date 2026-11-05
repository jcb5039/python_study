# 10장 문제 3 정답
#
# 해설:
# - set(nums)로 중복이 사라져요. len()으로 개수, sorted()로 정렬된 리스트.
# - sorted()는 집합을 넣어도 리스트를 돌려줘요.
# - common: 교집합 & 를 쓰면 둘 다 있는 값만 남아요.
#
# 다른 풀이 (common, 집합 연산 없이):
#   b_set = set(b)
#   result = set()
#   for x in a:
#       if x in b_set:
#           result.add(x)
#   return sorted(result)


def count_unique(nums):
    return len(set(nums))


def unique_sorted(nums):
    return sorted(set(nums))


def common(a, b):
    return sorted(set(a) & set(b))


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
