# 10장 문제 1: 장바구니 합계
#
# 장바구니(cart)에는 산 물건 이름이 들어 있고, 가격표(prices)는 딕셔너리예요.
# 장바구니의 전체 금액을 돌려주세요. 같은 물건이 여러 번 들어 있을 수 있어요.
# 가격표에 없는 물건은 0원으로 쳐요.
#
#   cart_total(['사과', '우유', '사과'], {'사과': 1200, '우유': 2500}) → 4900
#
# 채점: python3 exercises/ch10/ex01_cart.py
# 힌트: 강의 10장 "없는 키를 꺼내면 에러: get으로 안전하게"


def cart_total(cart, prices):
    pass  # TODO


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
