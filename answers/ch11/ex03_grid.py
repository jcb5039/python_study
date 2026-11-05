# 11장 문제 3 정답
#
# 해설:
# - grid_sum: 반복문 두 번(줄 → 칸). 다른 풀이: sum([sum(row) for row in grid]) 또는 sum(row_sums(grid))
# - row_sums: 줄 하나(row)는 그냥 리스트라서 sum(row)
# - col_sums: 열 j마다 모든 줄의 row[j]를 더해요. 칸 수는 len(grid[0])
#   for j in range(len(grid[0])):
#       total = 0
#       for row in grid:
#           total += row[j]
#   를 컴프리헨션으로 줄인 거예요.
# - zeros: [[0] * m] * n 은 같은 줄을 n번 가리켜서, 한 칸을 바꾸면 모든 줄이 바뀌어요.
#   줄마다 새로 만들어야 해요 → for _ in range(n)


def grid_sum(grid):
    total = 0
    for row in grid:
        for x in row:
            total += x
    return total


def row_sums(grid):
    return [sum(row) for row in grid]


def col_sums(grid):
    return [sum([row[j] for row in grid]) for j in range(len(grid[0]))]


def zeros(n, m):
    return [[0] * m for _ in range(n)]


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
