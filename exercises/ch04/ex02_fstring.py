# 4장 문제 2: f-string으로 문장 만들기
#
# None 자리에 f-string을 쓰세요. 기대하는 문장과 띄어쓰기까지 똑같아야 해요.
#
# 채점: python3 exercises/ch04/ex02_fstring.py
# 힌트: 강의 4장 "f-string: 문자열에 변수 넣기", "소수점 자릿수 정하기"

name = '민지'
km = 7.5
minutes = 42
price = 1500
count = 4
ratio = 2 / 3

# (1) → '민지님 안녕하세요'
greeting = None

# (2) → '민지님이 7.5km를 42분 동안 달렸어요'
record = None

# (3) → '합계: 6000원'   (price와 count를 곱해서)
total = None

# (4) → '비율: 0.67'     (ratio를 소수점 2자리로)
ratio_text = None

# (5) → '거리: 7.50km'   (km를 소수점 2자리로)
km_text = None

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('greeting', greeting, '민지님 안녕하세요')
check('record', record, '민지님이 7.5km를 42분 동안 달렸어요')
check('total', total, '합계: 6000원')
check('ratio_text', ratio_text, '비율: 0.67')
check('km_text', km_text, '거리: 7.50km')
