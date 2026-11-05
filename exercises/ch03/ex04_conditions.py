# 3장 문제 4: 조건 만들기
#
# None 자리에 비교 연산자와 and / or / not 을 써서 조건을 만드세요.
# True나 False를 직접 쓰지 말고, 아래 변수로 식을 만들어야 해요.
#
# 채점: python3 exercises/ch03/ex04_conditions.py
# 힌트: 강의 3장 "비교 연산자", "논리 연산자", "범위를 한 번에 비교하기"

age = 17
height = 145
is_member = False
points = 1200

# (1) 놀이기구: 나이가 12살 이상이고 키가 140 이상이어야 탈 수 있어요.
can_ride = None

# (2) 청소년: 나이가 13살 이상 19살 이하예요.
is_teen = None

# (3) 할인: 회원이거나 포인트가 1000 이상이면 할인받아요.
gets_discount = None

# (4) 성인: 나이가 19살 이상이에요.
is_adult = None

# (5) 회원이 아니에요. (not 을 쓰세요)
not_member = None

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('can_ride', can_ride, True)
check('is_teen', is_teen, True)
check('gets_discount', gets_discount, True)
check('is_adult', is_adult, False)
check('not_member', not_member, True)
