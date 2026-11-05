# 11장 문제 3: 2차원 리스트
#
# grid는 [[1, 2, 3], [4, 5, 6]] 같은 표예요. 모든 줄의 칸 수는 같아요.
#
# 채점: python3 exercises/ch11/ex03_grid.py
# 힌트: 강의 11장 "2차원 리스트: 표 만들기"


# (1) 표의 모든 칸의 합
#     grid_sum([[1, 2, 3], [4, 5, 6]]) → 21
def grid_sum(grid):
    pass  # TODO


# (2) 줄(행)마다의 합을 담은 리스트
#     row_sums([[1, 2, 3], [4, 5, 6]]) → [6, 15]
def row_sums(grid):
    pass  # TODO


# (3) 칸(열)마다의 합을 담은 리스트
#     col_sums([[1, 2, 3], [4, 5, 6]]) → [5, 7, 9]
#     힌트: 열 번호 j를 0부터 칸 수-1까지 돌면서, 모든 줄의 j번 칸을 더해요.
def col_sums(grid):
    pass  # TODO


# (4) n줄 m칸짜리, 모든 칸이 0인 표를 만들어 돌려주세요.
#     zeros(2, 3) → [[0, 0, 0], [0, 0, 0]]
#     ⚠️ 강의의 "빈 표를 만들 때 함정"을 꼭 읽고 푸세요. 채점에서 함정을 확인해요!
def zeros(n, m):
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

G = [[1, 2, 3], [4, 5, 6]]
check(grid_sum, (G,), 21)
check(grid_sum, ([[7]],), 7)
check(row_sums, (G,), [6, 15])
check(col_sums, (G,), [5, 7, 9])
check(col_sums, ([[1], [2], [3]],), [6])
check(zeros, (2, 3), [[0, 0, 0], [0, 0, 0]])


def zeros_trap_test(n, m):
    # 첫 칸만 1로 바꿨을 때 다른 줄은 그대로 0이어야 해요.
    table = zeros(n, m)
    table[0][0] = 1
    return table


check(zeros_trap_test, (2, 2), [[1, 0], [0, 0]])
