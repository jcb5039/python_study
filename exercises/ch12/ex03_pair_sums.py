# 12장 문제 3: 두 수를 골라 만들 수 있는 합 (함수형)
#
# 정수 리스트 numbers가 주어져요. 서로 다른 위치에 있는 두 수를 골라 더해서 만들 수 있는
# 모든 합을, 중복 없이 작은 수부터 정렬한 리스트로 return 하세요.
#
# [제한] numbers의 길이는 2 이상 100 이하, 각 수는 0 이상 100 이하
#
# [입출력 예]
#   numbers             result
#   [2, 1, 3, 4, 1]     [2, 3, 4, 5, 6, 7]
#   [5, 0, 2, 7]        [2, 5, 7, 9, 12]
#
#   첫 번째 예: 1+1=2, 2+1=3, 1+3=4, 1+4=5, 2+4=6, 3+4=7 ... 중복을 없애면 [2, 3, 4, 5, 6, 7]
#
# 채점: python3 exercises/ch12/ex03_pair_sums.py
# 힌트: 길이가 최대 100이라서 반복문 두 개를 겹쳐도 괜찮아요. (강의 12장 "제한 조건과 시간")
#       "서로 다른 위치"에서 고르려면 두 번째 반복을 i + 1부터 시작해 보세요.
#       중복 제거는 10장 집합!


def solution(numbers):
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

check(solution, ([2, 1, 3, 4, 1],), [2, 3, 4, 5, 6, 7])
check(solution, ([5, 0, 2, 7],), [2, 5, 7, 9, 12])
check(solution, ([3, 3],), [6])
check(solution, ([0, 0, 0],), [0])
