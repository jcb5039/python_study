# 10장 문제 4: 가장 많이 나온 글자
#
# 영어 소문자로 된 문자열을 받아서, 가장 많이 나온 글자를 돌려주세요.
# 가장 많이 나온 글자가 여러 개면, 문자열에서 먼저 나온 글자를 돌려주세요.
# 문자열은 비어 있지 않아요.
#
#   most_common('banana') → 'a'
#   most_common('abba') → 'a'    (a와 b 둘 다 2번이지만 a가 먼저 나왔어요)
#
# 채점: python3 exercises/ch10/ex04_most_common.py
# 힌트: 강의 10장 "딕셔너리로 개수 세기", "가장 많이 나온 것 찾기"
#       개수를 다 센 다음, "먼저 나온 순서"는 원래 문자열을 다시 돌면서 찾으면 쉬워요.


def most_common(s):
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

check(most_common, ('banana',), 'a')
check(most_common, ('abba',), 'a')
check(most_common, ('baab',), 'b')
check(most_common, ('z',), 'z')
check(most_common, ('mississippi',), 'i')
