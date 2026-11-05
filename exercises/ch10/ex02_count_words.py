# 10장 문제 2: 단어 개수 세기
#
# 띄어쓰기로 나뉜 문장을 받아서, 단어마다 몇 번 나왔는지 딕셔너리로 돌려주세요.
#
#   count_words('나는 나는 파이썬') → {'나는': 2, '파이썬': 1}
#
# 채점: python3 exercises/ch10/ex02_count_words.py
# 힌트: 강의 10장 "딕셔너리로 개수 세기" + 4장 split()


def count_words(sentence):
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

check(count_words, ('나는 나는 파이썬',), {'나는': 2, '파이썬': 1})
check(count_words, ('a b a c b a',), {'a': 3, 'b': 2, 'c': 1})
check(count_words, ('하나',), {'하나': 1})
check(count_words, ('',), {})
