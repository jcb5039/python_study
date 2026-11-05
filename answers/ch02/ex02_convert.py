# 2장 문제 2 정답
#
# 해설:
# - int('25') → 25: 글자를 정수로 바꿔야 더하기 같은 계산을 할 수 있어요.
# - str(price) + '원': 숫자와 글자는 + 로 이어 붙일 수 없어서(TypeError), 숫자를 먼저 글자로 바꿔요.
# - float('5.5') → 5.5: 소수점이 있는 글자는 float로 바꿔요. int('5.5')는 ValueError가 나요.
# - int(9.99) → 9: 정수로 바꾸면 소수점 아래를 반올림하지 않고 그냥 버려요.
#
# 자주 틀리는 점:
# - next_age = text_age + 1 → TypeError. 글자에는 숫자를 더할 수 없어요.
# - price_text = price + '원' → TypeError. 같은 이유예요.

text_age = '25'
price = 3000
text_km = '5.5'

age = int(text_age)
next_age = age + 1
price_text = str(price) + '원'
km = float(text_km)
cut = int(9.99)

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
