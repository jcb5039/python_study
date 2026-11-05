# 9장 문제 3: 모음 개수 세기
#
# 영어 소문자로 된 문자열 s를 받아서, 모음(a, e, i, o, u)이 몇 개인지 돌려주세요.
#   count_vowels('banana') → 3
#   count_vowels('sky') → 0
#
# 채점: python3 exercises/ch09/ex03_count_vowels.py
# 힌트: 강의 7장 "문자열을 한 글자씩 반복하기" + 4장 "들어 있는지 확인: in"
#       어떤 글자 ch가 모음인지는 ch in 'aeiou' 로 확인할 수 있어요.


def count_vowels(s):
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

check(count_vowels, ('banana',), 3)
check(count_vowels, ('sky',), 0)
check(count_vowels, ('aeiou',), 5)
check(count_vowels, ('',), 0)
check(count_vowels, ('programming',), 3)
