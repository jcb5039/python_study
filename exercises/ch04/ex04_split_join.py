# 4장 문제 4: 나누고 합치기
#
# None 자리에 split, join, 형변환을 써서 식을 만드세요.
#
# 채점: python3 exercises/ch04/ex04_split_join.py
# 힌트: 강의 4장 "나누기와 합치기"

date = '2026-11-04'
sentence = '나는 매일 파이썬을 공부한다'
score_text = '85 92'

# (1) date를 '-'로 나누기 → ['2026', '11', '04']
parts = None

# (2) 위의 parts를 '/'로 합치기 → '2026/11/04'
slash_date = None

# (3) date에서 '-'를 지운 글자 → '20261104'   (방법이 두 가지 있어요: replace 또는 split + join)
compact = None

# (4) sentence를 띄어쓰기로 나눴을 때 두 번째 단어 → '매일'
second_word = None

# (5) score_text의 두 점수를 정수로 바꿔 더한 값 → 177
#     한 줄에 다 쓰기 어려우면 TODO 자리에 변수를 더 만들어도 돼요.
# TODO

score_sum = None

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
