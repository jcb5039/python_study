# 3장 문제 1: 장보기 계산
#
# 할 일: (1)~(4)의 None을 지우고, 그 자리에 계산식을 쓰세요.
# 규칙: 7700처럼 답 숫자를 직접 쓰면 안 돼요. apple, banana, milk, paid와
#       앞에서 구한 변수(total, change)를 써서 식을 만드세요.
#
# 채점: python3 exercises/ch03/ex01_shopping.py
# 힌트: 강의 3장 "산술 연산자", "몫과 나머지는 이런 데 써요"

apple = 1200    # 사과 1개 값
banana = 800    # 바나나 1개 값
milk = 2500     # 우유 1개 값
paid = 10000    # 낸 돈

# (1) 사과 3개, 바나나 2개, 우유 1개를 샀어요. 전체 금액을 구하는 식을 쓰세요.
total = 7700

# (2) 10000원(paid)을 냈어요. 거스름돈을 구하는 식을 쓰세요.
change = 2300

# (3) 거스름돈(change)을 1000원짜리 지폐로 최대한 많이 받으면 몇 장인지 구하는 식을 쓰세요.
bills = 2

# (4) 1000원짜리로 받고 남는 돈을 구하는 식을 쓰세요.
coins = 300

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('total', total, 7700)
check('change', change, 2300)
check('bills', bills, 2)
check('coins', coins, 300)
