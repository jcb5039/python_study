# 3장 문제 1 정답
#
# 해설:
# - total: 곱하기가 더하기보다 먼저라서 괄호 없이 써도 돼요. 1200*3 + 800*2 + 2500 = 7700
# - change: 10000 - 7700 = 2300
# - bills: 2300을 1000씩 묶으면 몇 묶음? → 몫 // → 2
# - coins: 묶고 남은 것 → 나머지 % → 300
#
# 자주 틀리는 점:
# - bills = change / 1000 → 2.3 (float). 장 수는 정수여야 하니까 // 를 써요.

apple = 1200
banana = 800
milk = 2500
paid = 10000

total = apple * 3 + banana * 2 + milk
change = paid - total
bills = change // 1000
coins = change % 1000

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
