# 2장 문제 4 정답
#
# 해설:
# - q1 3.0: 소수점이 있으면 뒤가 0이어도 float
# - q2 '3.0': 따옴표가 있으면 숫자처럼 생겨도 str
# - q3 False: bool (True, False 딱 두 개)
# - q4 -15: 음수도 소수점이 없으면 int
# - q5 '': 빈 문자열도 str
# - q6 'True': 따옴표 안의 True는 글자! str
# - q7 int('8'): 정수로 바꿨으니 int
# - q8 str(8): 글자로 바꿨으니 str
# - q9 10 / 2: 결과는 5가 아니라 5.0 → float
#   파이썬에서 / 나누기는 딱 떨어져도 항상 실수를 돌려줘요. 3장에서 자세히 배워요.

q0 = 'int'
q1 = 'float'
q2 = 'str'
q3 = 'bool'
q4 = 'int'
q5 = 'str'
q6 = 'str'
q7 = 'int'
q8 = 'str'
q9 = 'float'

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('q0 (7)', q0, type(7).__name__)
check('q1 (3.0)', q1, type(3.0).__name__)
check("q2 ('3.0')", q2, type('3.0').__name__)
check('q3 (False)', q3, type(False).__name__)
check('q4 (-15)', q4, type(-15).__name__)
check("q5 ('')", q5, type('').__name__)
check("q6 ('True')", q6, type('True').__name__)
check("q7 (int('8'))", q7, type(int('8')).__name__)
check('q8 (str(8))', q8, type(str(8)).__name__)
check('q9 (10 / 2)', q9, type(10 / 2).__name__)
