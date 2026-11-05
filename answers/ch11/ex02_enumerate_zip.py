# 11장 문제 2 정답
#
# 해설:
# - numbered: enumerate(names, start=1)로 1부터 번호를 받아요.
# - to_dict: zip으로 짝지어 돌면서 딕셔너리에 넣어요.
#   (한 줄 풀이: return dict(zip(names, scores)) ← dict()는 짝들을 딕셔너리로 바꿔 줘요)
# - add_pairs: zip으로 같은 번호끼리 꺼내서 더해요.
# - find_all: 번호가 필요하니까 enumerate. 조건에 맞는 번호(i)만 담아요.


def numbered(names):
    return [f'{i}. {name}' for i, name in enumerate(names, start=1)]


def to_dict(names, scores):
    result = {}
    for name, score in zip(names, scores):
        result[name] = score
    return result


def add_pairs(a, b):
    return [x + y for x, y in zip(a, b)]


def find_all(nums, target):
    return [i for i, x in enumerate(nums) if x == target]


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

check(numbered, (['민지', '철수'],), ['1. 민지', '2. 철수'])
check(numbered, ([],), [])
check(to_dict, (['민지', '철수'], [90, 85]), {'민지': 90, '철수': 85})
check(add_pairs, ([1, 2, 3], [10, 20, 30]), [11, 22, 33])
check(find_all, ([5, 3, 5, 1, 5], 5), [0, 2, 4])
check(find_all, ([1, 2], 9), [])
