# 4장 문제 2 정답
#
# 해설:
# - 따옴표 앞에 f를 붙이고, 넣고 싶은 변수나 계산을 { } 로 감싸요.
# - { } 안에서 계산도 돼요: {price * count}
# - {값:.2f} 는 소수점 2자리까지 반올림. 7.5 → 7.50 처럼 0도 채워 줘요.
#
# 자주 틀리는 점:
# - f를 빼먹으면 '{name}님 안녕하세요' 가 글자 그대로 들어가요.
# - '합계: ' 의 콜론 뒤 띄어쓰기를 빼먹기 쉬워요.

name = '민지'
km = 7.5
minutes = 42
price = 1500
count = 4
ratio = 2 / 3

greeting = f'{name}님 안녕하세요'
record = f'{name}님이 {km}km를 {minutes}분 동안 달렸어요'
total = f'합계: {price * count}원'
ratio_text = f'비율: {ratio:.2f}'
km_text = f'거리: {km:.2f}km'

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
