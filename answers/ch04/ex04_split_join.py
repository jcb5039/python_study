# 4장 문제 4 정답
#
# 해설:
# - split('-'): '-' 를 기준으로 잘라서 리스트로
# - '/'.join(parts): 사이에 '/' 를 넣어서 합치기. 넣을 글자를 앞에 써요.
# - compact: date.replace('-', '') 도 되고, ''.join(date.split('-')) 도 돼요.
# - second_word: split() 결과의 1번 (0번이 첫 번째니까)
# - score_sum: 나눈 조각은 문자열이라서 int()로 바꾼 뒤 더해요.
#   '85' + '92' 는 '8592' 가 돼 버려요.

date = '2026-11-04'
sentence = '나는 매일 파이썬을 공부한다'
score_text = '85 92'

parts = date.split('-')
slash_date = '/'.join(parts)
compact = date.replace('-', '')
second_word = sentence.split()[1]

a, b = score_text.split()
score_sum = int(a) + int(b)

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('parts', parts, ['2026', '11', '04'])
check('slash_date', slash_date, '2026/11/04')
check('compact', compact, '20261104')
check('second_word', second_word, '매일')
check('score_sum', score_sum, 177)
