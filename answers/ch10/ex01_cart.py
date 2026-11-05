# 10장 문제 1 정답
#
# 해설:
# - 장바구니를 돌면서 물건마다 가격을 찾아 더해요.
# - prices[item] 을 쓰면 '딸기'처럼 없는 물건에서 KeyError가 나요.
#   prices.get(item, 0) 은 없으면 0을 돌려줘서 안전해요.


def cart_total(cart, prices):
    total = 0
    for item in cart:
        total += prices.get(item, 0)
    return total


# ───── 채점 코드 ─────
# 9장까지 배웠다면 이제 읽을 수 있어요! (try/except는 에러가 나도 멈추지 않게 하는 문법이에요)

def check(func, args, expected):
    call = f"{func.__name__}({', '.join(repr(a) for a in args)})"
    try:
        actual = func(*args)
    except Exception as e:
        print(f'❌ {call}  에러: {type(e).__name__}: {e}')
        return
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {call}')
    else:
        print(f'❌ {call}  결과: {actual!r}  기대: {expected!r}')

PRICES = {'사과': 1200, '바나나': 800, '우유': 2500}
check(cart_total, (['사과', '우유', '사과'], PRICES), 4900)
check(cart_total, ([], PRICES), 0)
check(cart_total, (['바나나'], PRICES), 800)
check(cart_total, (['사과', '딸기'], PRICES), 1200)
