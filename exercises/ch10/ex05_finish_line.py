# 10장 문제 5: 결승선을 못 넘은 사람
#
# 마라톤 출발 명단(starters)과 결승선 도착 명단(finishers)이 주어져요.
# 딱 한 명만 결승선을 넘지 못했어요. 그 사람의 이름을 돌려주세요.
# 이름이 같은 사람(동명이인)이 있을 수 있어요!
#
#   not_finished(['민지', '철수', '영희'], ['영희', '민지']) → '철수'
#   not_finished(['민지', '민지', '철수'], ['민지', '철수']) → '민지'
#
# 채점: python3 exercises/ch10/ex05_finish_line.py
# 힌트: 강의 10장 "딕셔너리로 개수 세기"
#       출발한 사람은 +1, 도착한 사람은 -1 하면, 끝에 1이 남는 사람이 있어요.
#       (finishers.remove()로 풀어도 답은 나오지만, 명단이 길면 아주 느려요. 12장에서 이유를 배워요.)


def not_finished(starters, finishers):
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

check(not_finished, (['민지', '철수', '영희'], ['영희', '민지']), '철수')
check(not_finished, (['민지', '민지', '철수'], ['민지', '철수']), '민지')
check(not_finished, (['a'], []), 'a')
check(not_finished, (['a', 'b', 'a', 'b'], ['b', 'a', 'b']), 'a')
