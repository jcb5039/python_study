# 10장 문제 2 정답
#
# 해설:
# - split()으로 단어 리스트를 만들고, 개수 세기 패턴을 그대로 써요.
# - 빈 문자열은 ''.split() → [] 이라서 반복을 안 하고 빈 딕셔너리가 나와요.
#
# 다른 풀이 (if로 처음인지 확인):
#   if word in counts:
#       counts[word] += 1
#   else:
#       counts[word] = 1


def count_words(sentence):
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


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

check(count_words, ('나는 나는 파이썬',), {'나는': 2, '파이썬': 1})
check(count_words, ('a b a c b a',), {'a': 3, 'b': 2, 'c': 1})
check(count_words, ('하나',), {'하나': 1})
check(count_words, ('',), {})
