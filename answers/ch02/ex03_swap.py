# 2장 문제 3 정답
#
# 해설:
# - a = b 를 먼저 하면 a의 원래 값('왼쪽')이 사라져서 b에 넣을 수 없어요.
# - 방법 1: temp 같은 임시 변수에 a를 잠깐 맡겨 두고 옮겨요.
#     temp = a
#     a = b
#     b = temp
# - 방법 2 (아래): a, b = b, a
#   오른쪽 b, a 를 먼저 전부 계산한 다음('오른쪽', '왼쪽') 왼쪽 a, b에 차례로 넣어요.
#   파이썬에서 가장 많이 쓰는 방법이에요.

a = '왼쪽'
b = '오른쪽'

a, b = b, a

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('a', a, '오른쪽')
check('b', b, '왼쪽')
