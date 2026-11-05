# 4장 문제 3: 문자열 메서드
#
# None 자리에 메서드를 써서 식을 만드세요.
#
# 채점: python3 exercises/ch04/ex03_methods.py
# 힌트: 강의 4장 "문자열 기능 (메서드)"

raw = '   Hello Python   '
fruit = 'banana'
email = 'runner@test.com'

# (1) raw의 양쪽 공백을 지우기 → 'Hello Python'
cleaned = None

# (2) 위의 cleaned를 전부 대문자로 → 'HELLO PYTHON'
loud = None

# (3) fruit에 'a'가 몇 개? → 3
a_count = None

# (4) fruit의 'a'를 전부 'o'로 바꾸기 → 'bonono'
changed = None

# (5) email에 '@'가 들어 있는지 → True   (in 을 쓰세요)
has_at = None

# (6) email에서 '@'가 몇 번째 자리에 있는지 → 6
at_index = None

# (7) 도전! email에서 '@' 앞부분만 꺼내기 → 'runner'
#     (6)에서 구한 at_index와 슬라이싱을 같이 써 보세요.
user_id = None

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('cleaned', cleaned, 'Hello Python')
check('loud', loud, 'HELLO PYTHON')
check('a_count', a_count, 3)
check('changed', changed, 'bonono')
check('has_at', has_at, True)
check('at_index', at_index, 6)
check('user_id', user_id, 'runner')
