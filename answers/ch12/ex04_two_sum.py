# 12장 문제 4 정답
#
# 해설:
# - 반복문 두 개 겹침: 길이 10만이면 약 50억 번 비교 → 시간 초과.
# - 숫자 x를 볼 때 필요한 짝은 target - x 하나뿐이에요.
#   지금까지 본 수를 집합(seen)에 넣어 두면, "짝이 앞에 있었나?"를 바로 확인할 수 있어요.
# - 확인을 먼저 하고 add를 나중에 해요. 그래야 x 자기 자신을 짝으로 쓰지 않아요.
#   ([4]와 target 8에서, 4를 넣기 전에 확인하니까 False가 맞게 나와요)
#   ([4, 4]에서는 두 번째 4를 볼 때 첫 번째 4가 seen에 있어서 True)
# - 리스트로 seen을 만들면 in이 느려서 결국 시간 초과예요. 집합이어야 해요.
#
# 이렇게 "앞에서 본 것을 집합/딕셔너리에 기억해 두기"는 코딩테스트에서 정말 자주 쓰는 방법이에요.


def solution(nums, target):
    seen = set()
    for x in nums:
        if target - x in seen:
            return True
        seen.add(x)
    return False

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
