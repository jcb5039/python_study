# 11장 문제 4: 기준을 정해서 정렬하기
#
# 채점: python3 exercises/ch11/ex04_sort_key.py
# 힌트: 강의 11장 "정렬 기준 정하기: key", "기준 두 개"


# (1) 단어들을 짧은 것부터 정렬. 길이가 같으면 원래 순서 그대로.
#     by_length(['banana', 'kiwi', 'fig']) → ['fig', 'kiwi', 'banana']
def by_length(words):
    pass  # TODO


# (2) (이름, 점수) 리스트를 점수 높은 순으로, 점수가 같으면 이름 가나다(ABC)순으로 정렬한 뒤
#     이름만 담은 리스트를 돌려주세요.
#     ranking([('철수', 85), ('영희', 90), ('민지', 90)]) → ['민지', '영희', '철수']
def ranking(students):
    pass  # TODO


# (3) 좌표 (x, y) 리스트를 원점(0, 0)에서 가까운 순으로 정렬해서 돌려주세요.
#     거리는 x * x + y * y 로 비교하면 돼요. 거리가 같으면 x가 작은 것부터.
#     by_distance([(3, 4), (1, 1), (-1, 1)]) → [(-1, 1), (1, 1), (3, 4)]
def by_distance(points):
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

check(by_length, (['banana', 'kiwi', 'fig'],), ['fig', 'kiwi', 'banana'])
check(by_length, (['bb', 'a', 'cc'],), ['a', 'bb', 'cc'])
check(ranking, ([('철수', 85), ('영희', 90), ('민지', 90)],), ['민지', '영희', '철수'])
check(ranking, ([('b', 1), ('a', 1), ('c', 2)],), ['c', 'a', 'b'])
check(by_distance, ([(3, 4), (1, 1), (-1, 1)],), [(-1, 1), (1, 1), (3, 4)])
check(by_distance, ([(0, 5), (5, 0), (0, 0)],), [(0, 0), (0, 5), (5, 0)])
