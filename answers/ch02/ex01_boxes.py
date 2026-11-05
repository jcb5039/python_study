# 2장 문제 1 정답
#
# 해설:
# - 글자는 따옴표로 감싸고, 숫자는 따옴표 없이, True는 첫 글자를 대문자로 써요.
# - next_year = year + 1: 오른쪽(year + 1 → 2027)을 먼저 계산해서 왼쪽에 넣어요.
#   2027이라고 직접 써도 결과는 같지만, year가 바뀌면 같이 바뀌도록 변수로 계산하는 습관이 좋아요.
#
# 자주 틀리는 점:
# - year = '2026' 처럼 따옴표를 붙이면 글자가 돼서 ❌ (기대한 건 정수 2026)
# - is_student = true → NameError (True는 대문자로 시작)

city = '서울'
year = 2026
height = 172.5
is_student = True
next_year = year + 1

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('city', city, '서울')
check('year', year, 2026)
check('height', height, 172.5)
check('is_student', is_student, True)
check('next_year', next_year, 2027)
