# 11장 문제 4 정답
#
# 해설:
# - by_length: key=len. 파이썬 정렬은 기준이 같으면 원래 순서를 지켜 줘요(안정 정렬).
# - ranking: 기준 두 개를 튜플로. 점수는 높은 게 먼저라서 -s[1], 이름은 오름차순이라 s[0].
#   정렬한 다음 이름만 컴프리헨션으로 꺼내요.
# - by_distance: (거리, x) 튜플을 기준으로.
#   p[0]이 x, p[1]이 y예요.
#
# 자주 틀리는 점:
# - ranking에서 reverse=True를 쓰면 이름도 거꾸로(철수 > 영희 > 민지) 정렬돼요.


def by_length(words):
    return sorted(words, key=len)


def ranking(students):
    ordered = sorted(students, key=lambda s: (-s[1], s[0]))
    return [name for name, score in ordered]


def by_distance(points):
    return sorted(points, key=lambda p: (p[0] * p[0] + p[1] * p[1], p[0]))


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

check(by_length, (['banana', 'kiwi', 'fig'],), ['fig', 'kiwi', 'banana'])
check(by_length, (['bb', 'a', 'cc'],), ['a', 'bb', 'cc'])
check(ranking, ([('철수', 85), ('영희', 90), ('민지', 90)],), ['민지', '영희', '철수'])
check(ranking, ([('b', 1), ('a', 1), ('c', 2)],), ['c', 'a', 'b'])
check(by_distance, ([(3, 4), (1, 1), (-1, 1)],), [(-1, 1), (1, 1), (3, 4)])
check(by_distance, ([(0, 5), (5, 0), (0, 0)],), [(0, 0), (0, 5), (5, 0)])
