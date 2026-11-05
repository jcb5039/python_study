# 2장 문제 1: 변수 만들기
#
# None 자리를 지우고, 설명에 맞는 값을 넣으세요.
#
# 채점: python3 exercises/ch02/ex01_boxes.py
# 힌트: 강의 2장 "자료형: 값의 종류"

# (1) 도시 이름 '서울'을 담으세요. (글자)
city = None

# (2) 올해 연도 2026을 담으세요. (정수)
year = None

# (3) 키 172.5를 담으세요. (실수)
height = None

# (4) "학생이다"가 참이라는 값을 담으세요. (참거짓)
is_student = None

# (5) 내년 연도를 담으세요. 2027을 직접 쓰지 말고, 위에서 만든 year를 이용해 계산하세요.
next_year = None

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
