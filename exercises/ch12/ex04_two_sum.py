# 12장 문제 4: 합이 target인 두 수 (함수형, 시간 측정)
#
# 정수 리스트 nums와 정수 target이 주어져요.
# 서로 다른 위치에 있는 두 수를 골라 더해서 target을 만들 수 있으면 True, 없으면 False를 return 하세요.
#
# [제한] nums의 길이는 1 이상 100,000 이하 / 각 수와 target은 -1,000,000,000 이상 1,000,000,000 이하
#
# [입출력 예]
#   nums             target    result
#   [2, 7, 11, 15]   9         True     (2 + 7)
#   [3, 1, 4]        8         False
#   [4, 4]           8         True     (서로 다른 위치의 4와 4)
#   [4]              8         False    (4 하나를 두 번 쓸 수는 없어요)
#
# 채점: python3 exercises/ch12/ex04_two_sum.py
#       채점 데이터에 길이 10만짜리 리스트가 있어요. 1초 안에 끝나야 해요!
#
# 힌트 (하나씩만 열어 보세요):
#   1. 반복문 두 개를 겹치면 10만 × 10만 = 100억 번. 너무 느려요. (강의 12장 "제한 조건과 시간")
#   2. 숫자 x를 볼 때, 짝이 될 수는 정확히 target - x 예요. "그 수가 앞에 있었나?"만 알면 돼요.
#   3. "앞에서 본 수"들을 집합에 넣어 두면 "있나?"를 바로 확인할 수 있어요. (강의 10장 집합, 12장 "해결: 집합과 딕셔너리")


def solution(nums, target):
    pass  # TODO

# ───── 채점 코드 ─────
# 시간도 재요. 1초가 넘으면 답이 맞아도 ❌예요. (실제 코딩테스트의 "시간 초과"와 같아요)
# 3초가 지나도 안 끝나면 기다리지 않고 멈춰요.

import signal
import time


class TooSlow(Exception):
    pass


def stop_running(signum, frame):
    raise TooSlow()


def check(func, args, expected, label=None):
    call = label or f"{func.__name__}({', '.join(repr(a) for a in args)})"
    can_stop = hasattr(signal, 'setitimer')
    if can_stop:
        signal.signal(signal.SIGALRM, stop_running)
        signal.setitimer(signal.ITIMER_REAL, 3)
    start = time.time()
    try:
        actual = func(*args)
    except TooSlow:
        print(f'❌ {call}  ⏱️ 3초가 지나도 끝나지 않아서 멈췄어요. (시간 초과)')
        return
    except Exception as e:
        print(f'❌ {call}  에러: {type(e).__name__}: {e}')
        return
    finally:
        if can_stop:
            signal.setitimer(signal.ITIMER_REAL, 0)
    seconds = time.time() - start
    if not (type(actual) == type(expected) and actual == expected):
        print(f'❌ {call}  결과: {actual!r}  기대: {expected!r}')
    elif seconds > 1:
        print(f'❌ {call}  답은 맞지만 ⏱️ {seconds:.1f}초 걸렸어요. 1초 안에 끝나야 해요.')
    else:
        print(f'✅ {call}  ({seconds:.3f}초)')

check(solution, ([2, 7, 11, 15], 9), True)
check(solution, ([3, 1, 4], 8), False)
check(solution, ([4, 4], 8), True)
check(solution, ([4], 8), False)
check(solution, ([-3, 10, 5], 2), True)

BIG = list(range(1, 100001))
check(solution, (BIG, 199999), True, 'solution(1~100000, 199999)')
check(solution, (BIG, 300000), False, 'solution(1~100000, 300000)')
