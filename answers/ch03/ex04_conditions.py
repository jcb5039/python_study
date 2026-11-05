# 3장 문제 4 정답
#
# 해설:
# - can_ride: 두 조건이 "모두" 맞아야 하니까 and
# - is_teen: 13 <= age <= 19 처럼 범위를 이어서 쓸 수 있어요.
#   age >= 13 and age <= 19 라고 써도 같아요.
# - gets_discount: 둘 중 "하나라도" 맞으면 되니까 or. is_member는 False지만 points가 1200이라 True
# - is_adult: 17 >= 19 → False
# - not_member: not False → True
#
# 자주 틀리는 점:
# - 이상/이하는 >=, <=, 초과/미만은 >, < 예요. "19살 이하"는 19도 포함이에요.

age = 17
height = 145
is_member = False
points = 1200

can_ride = age >= 12 and height >= 140
is_teen = 13 <= age <= 19
gets_discount = is_member or points >= 1000
is_adult = age >= 19
not_member = not is_member

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
