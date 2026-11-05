# 9장 문제 1 정답
#
# 해설:
# - 계산 결과를 return 뒤에 바로 써요.
# - greet는 문자열을 만들어서 돌려줘요. print(f'안녕, {name}!') 로 쓰면
#   화면에는 보이지만 돌려받는 값은 None이라 ❌가 나와요.


def add(a, b):
    return a + b


def square(n):
    return n * n


def greet(name):
    return f'안녕, {name}!'


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

check(add, (3, 5), 8)
check(add, (-1, 1), 0)
check(square, (4,), 16)
check(square, (-3,), 9)
check(greet, ('민지',), '안녕, 민지!')
check(greet, ('Python',), '안녕, Python!')
