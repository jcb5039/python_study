# 10장 문제 5 정답
#
# 해설:
# - 이름마다 "출발했는데 아직 도착 안 한 사람 수"를 딕셔너리에 기록해요.
#   출발 명단을 돌면서 +1, 도착 명단을 돌면서 -1.
# - 끝에 값이 1 이상(정확히는 1)인 이름이 답이에요.
# - 동명이인도 개수로 세기 때문에 문제없어요.
#   집합(set)으로 빼면 동명이인이 하나로 합쳐져서 틀려요.
#
# 다른 풀이 (정렬해서 비교):
#   starters = sorted(starters)
#   finishers = sorted(finishers)
#   for i in range(len(finishers)):
#       if starters[i] != finishers[i]:
#           return starters[i]
#   return starters[-1]


def not_finished(starters, finishers):
    counts = {}
    for name in starters:
        counts[name] = counts.get(name, 0) + 1
    for name in finishers:
        counts[name] -= 1

    for name, count in counts.items():
        if count > 0:
            return name


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

check(not_finished, (['민지', '철수', '영희'], ['영희', '민지']), '철수')
check(not_finished, (['민지', '민지', '철수'], ['민지', '철수']), '민지')
check(not_finished, (['a'], []), 'a')
check(not_finished, (['a', 'b', 'a', 'b'], ['b', 'a', 'b']), 'a')
