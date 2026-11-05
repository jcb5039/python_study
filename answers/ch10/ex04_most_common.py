# 10장 문제 4 정답
#
# 해설:
# - 1단계: 딕셔너리로 글자마다 개수를 세요.
# - 2단계: 원래 문자열 s를 앞에서부터 다시 돌면서 개수가 가장 큰 글자를 찾아요.
#   > (같으면 안 바꿈)를 쓰니까, 개수가 같으면 먼저 나온 글자가 그대로 남아요.
#   >= 를 쓰면 나중에 나온 글자로 바뀌어 버려요.
# - 'mississippi'는 i와 s가 둘 다 4번인데, i가 먼저 나와요(m 다음).


def most_common(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    best = s[0]
    for ch in s:
        if counts[ch] > counts[best]:
            best = ch
    return best


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

check(most_common, ('banana',), 'a')
check(most_common, ('abba',), 'a')
check(most_common, ('baab',), 'b')
check(most_common, ('z',), 'z')
check(most_common, ('mississippi',), 'i')
