# 11장 문제 2: 번호 붙이기, 두 리스트 짝짓기
#
# 채점: python3 exercises/ch11/ex02_enumerate_zip.py
# 힌트: 강의 11장 "enumerate", "zip"


# (1) 이름 리스트를 받아서 '1. 이름' 모양의 문자열 리스트를 돌려주세요.
#     numbered(['민지', '철수']) → ['1. 민지', '2. 철수']
def numbered(names):
    pass  # TODO


# (2) 이름 리스트와 점수 리스트를 받아서 {이름: 점수} 딕셔너리를 돌려주세요.
#     to_dict(['민지', '철수'], [90, 85]) → {'민지': 90, '철수': 85}
def to_dict(names, scores):
    pass  # TODO


# (3) 두 리스트에서 같은 번호끼리 더한 리스트를 돌려주세요.
#     add_pairs([1, 2, 3], [10, 20, 30]) → [11, 22, 33]
def add_pairs(a, b):
    pass  # TODO


# (4) 리스트에서 값이 target인 위치(번호)들을 리스트로 돌려주세요. 번호는 0부터예요.
#     find_all([5, 3, 5, 1, 5], 5) → [0, 2, 4]
def find_all(nums, target):
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

check(numbered, (['민지', '철수'],), ['1. 민지', '2. 철수'])
check(numbered, ([],), [])
check(to_dict, (['민지', '철수'], [90, 85]), {'민지': 90, '철수': 85})
check(add_pairs, ([1, 2, 3], [10, 20, 30]), [11, 22, 33])
check(find_all, ([5, 3, 5, 1, 5], 5), [0, 2, 4])
check(find_all, ([1, 2], 9), [])
