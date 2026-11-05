# 3장 문제 2 정답
#
# 해설:
# - hours = 7384 // 3600 = 2      (3600초 묶음이 2개)
# - left = 7384 % 3600 = 184      (2시간을 빼고 남은 초)
# - minutes = 184 // 60 = 3       (60초 묶음이 3개)
# - seconds = 184 % 60 = 4        (3분을 빼고 남은 초)
#   → 2시간 3분 4초
#
# 다른 풀이: seconds = total_seconds % 60 도 같은 답이에요. 3600은 60으로 나누어떨어지니까요.

total_seconds = 7384

hours = total_seconds // 3600
left = total_seconds % 3600
minutes = left // 60
seconds = left % 60

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('hours', hours, 2)
check('left', left, 184)
check('minutes', minutes, 3)
check('seconds', seconds, 4)
