# 2장 문제 2: 형변환하기
#
# None 자리를 지우고 알맞은 계산을 쓰세요.
#
# 채점: python3 exercises/ch02/ex02_convert.py
# 힌트: 강의 2장 "형변환: 다른 종류로 바꾸기"

text_age = '25'     # 글자로 된 나이
price = 3000        # 숫자로 된 가격
text_km = '5.5'     # 글자로 된 거리

# (1) text_age를 정수로 바꿔서 담으세요. → 25
age = None

# (2) 위의 age에 1을 더한 값을 담으세요. → 26
next_age = None

# (3) price 뒤에 '원'을 붙인 글자를 만드세요. → '3000원'
price_text = None

# (4) text_km를 실수로 바꿔서 담으세요. → 5.5
km = None

# (5) 9.99를 정수로 바꾼 값을 담으세요. 결과를 먼저 예측해 보세요!
cut = None

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('age', age, 25)
check('next_age', next_age, 26)
check('price_text', price_text, '3000원')
check('km', km, 5.5)
check('cut', cut, 9)
