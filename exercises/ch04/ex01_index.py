# 4장 문제 1: 인덱스와 슬라이싱
#
# None 자리에 word를 이용한 식을 쓰세요. ('p'처럼 답을 직접 쓰면 안 돼요!)
#
# 채점: python3 exercises/ch04/ex01_index.py
# 힌트: 강의 4장 "인덱스", "슬라이싱"

word = 'programming'

# (1) 첫 글자 → 'p'
first = None

# (2) 마지막 글자 → 'g'  (음수 번호를 써 보세요)
last = None

# (3) 앞에서 7글자 → 'program'
front = None

# (4) 뒤에서 4글자 → 'ming'
back = None

# (5) 거꾸로 뒤집기 → 'gnimmargorp'
reverse = None

# (6) 글자 수 → 11
length = None

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('first', first, 'p')
check('last', last, 'g')
check('front', front, 'program')
check('back', back, 'ming')
check('reverse', reverse, 'gnimmargorp')
check('length', length, 11)
