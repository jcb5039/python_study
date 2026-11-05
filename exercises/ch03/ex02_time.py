# 3장 문제 2: 초를 시간·분·초로 바꾸기
#
# 마라톤 기록이 7384초예요. 몇 시간 몇 분 몇 초일까요?
# None 자리에 계산식을 쓰세요. (1시간 = 3600초, 1분 = 60초)
#
# 채점: python3 exercises/ch03/ex02_time.py
# 힌트: 강의 3장 "몫과 나머지는 이런 데 써요" → 시간 바꾸기
#       시간을 먼저 구하고, 시간으로 묶고 남은 초에서 분을 구해요.

total_seconds = 7384

# (1) 몇 시간?
hours = None

# (2) 시간으로 묶고 남은 초는?
left = None

# (3) 남은 초(left)로 만든 분은?
minutes = None

# (4) 마지막에 남은 초는?
seconds = None

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
