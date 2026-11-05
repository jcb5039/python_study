# 2장 문제 3: 두 변수의 값 바꾸기
#
# a에는 '왼쪽', b에는 '오른쪽'이 들어 있어요.
# 아래 TODO 자리에 코드를 써서 a와 b의 값을 서로 바꾸세요.
#   바꾼 뒤: a는 '오른쪽', b는 '왼쪽'
#
# 규칙: a = '오른쪽' 처럼 값을 직접 쓰지 말고, 변수끼리 옮겨서 바꾸세요.
#
# 채점: python3 exercises/ch02/ex03_swap.py
# 힌트: 강의 2장 "두 변수의 값 바꾸기" (방법이 두 가지 있어요. 둘 다 해 보세요!)

a = '왼쪽'
b = '오른쪽'

# TODO: 여기에 코드를 쓰세요.


# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('a', a, '오른쪽')
check('b', b, '왼쪽')
