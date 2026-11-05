# 9장 문제 3 정답
#
# 해설:
# - 7장의 "개수 세기" 패턴을 함수 안에 넣은 거예요.
# - ch in 'aeiou': 글자 ch가 'aeiou' 안에 들어 있으면 True
# - return count 는 반복문이 다 끝난 다음(들여쓰기를 뺀 위치)에 써야 해요.
#
# 다른 풀이: 모음마다 count()를 더하기
#   return s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')


def count_vowels(s):
    count = 0
    for ch in s:
        if ch in 'aeiou':
            count += 1
    return count


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
