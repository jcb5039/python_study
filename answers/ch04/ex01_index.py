# 4장 문제 1 정답
#
# 해설:
# - first: 첫 글자는 0번
# - last: -1은 맨 뒤
# - front: [:7] 은 0번부터 6번까지 (7번은 포함 안 함) → 7글자
# - back: [-4:] 는 뒤에서 4번째부터 끝까지
#   다른 풀이: word[7:] (앞 7글자를 뺀 나머지)
# - reverse: [::-1] 은 간격 -1, 즉 뒤에서부터 한 칸씩
# - length: len()

word = 'programming'

first = word[0]
last = word[-1]
front = word[:7]
back = word[-4:]
reverse = word[::-1]
length = len(word)

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
