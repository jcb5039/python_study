# 9장 문제 4 정답
#
# 해설:
# - my_sum: total = 0 으로 시작해서 하나씩 더해요. 빈 리스트면 반복을 안 해서 0이 그대로 나와요.
# - my_max: biggest를 nums[0](첫 번째 값)으로 시작해요.
#   0으로 시작하면 [-5, -2, -9] 에서 0이 나와 버려요.
# - my_average: 함수 안에서 다른 함수(my_sum)를 불러 썼어요.
#   / 는 항상 float를 돌려주니까 [10, 20] 의 평균은 15가 아니라 15.0 이에요.


def my_sum(nums):
    total = 0
    for x in nums:
        total += x
    return total


def my_max(nums):
    biggest = nums[0]
    for x in nums:
        if x > biggest:
            biggest = x
    return biggest


def my_average(nums):
    return my_sum(nums) / len(nums)


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

check(my_sum, ([1, 2, 3],), 6)
check(my_sum, ([],), 0)
check(my_sum, ([-5, 5, 10],), 10)
check(my_max, ([3, 9, 2],), 9)
check(my_max, ([7],), 7)
check(my_max, ([-5, -2, -9],), -2)
check(my_average, ([1, 2, 3, 4],), 2.5)
check(my_average, ([10, 20],), 15.0)
