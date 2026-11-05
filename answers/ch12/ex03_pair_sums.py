# 12장 문제 3 정답
#
# 해설:
# - i는 첫 번째 수의 위치, j는 두 번째 수의 위치. j를 i + 1부터 시작하면
#   같은 위치를 두 번 고르지도 않고, (i, j)와 (j, i)를 중복해서 보지도 않아요.
# - 합들을 집합에 넣으면 중복이 저절로 사라지고, sorted()로 정렬된 리스트가 돼요.
# - 길이가 100이면 반복은 약 100 * 100 / 2 = 5,000번. 아주 빨라요.
#
# 자주 틀리는 점:
# - j를 0부터 돌리면 i == j일 때 같은 수를 두 번 더해요. ([3, 3]이 아니라 [5]만 있어도 10이 나옴)
# - return sorted(sums) 대신 return sums 를 하면 집합이 나와서 ❌


def solution(numbers):
    sums = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sums.add(numbers[i] + numbers[j])
    return sorted(sums)


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

check(solution, ([2, 1, 3, 4, 1],), [2, 3, 4, 5, 6, 7])
check(solution, ([5, 0, 2, 7],), [2, 5, 7, 9, 12])
check(solution, ([3, 3],), [6])
check(solution, ([0, 0, 0],), [0])
