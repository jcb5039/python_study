# 3장 문제 2: 초를 시간·분·초로 바꾸기
#
# 마라톤 기록이 7384초예요. 몇 시간 몇 분 몇 초일까요?
# 할 일: (1)~(4)를 순서대로 구해서 7384초를 '몇 시간 몇 분 몇 초'로 바꾸세요.
#        None을 지우고, 그 자리에 계산식을 쓰세요. (1시간 = 3600초, 1분 = 60초)
# 규칙: 숫자 답을 직접 쓰지 말고 total_seconds와 앞에서 구한 변수로 계산하세요.
#
# 채점: python3 exercises/ch03/ex02_time.py
# 힌트: 강의 3장 "몫과 나머지는 이런 데 써요" → 시간 바꾸기
#       시간을 먼저 구하고, 시간으로 묶고 남은 초에서 분을 구해요.

total_seconds = 7384

# (1) total_seconds가 몇 시간인지 구하는 식을 쓰세요.
hours = 7884 // 3600

# (2) total_seconds를 시간으로 묶고 남는 초를 구하는 식을 쓰세요.
left = 184

# (3) 남은 초(left)가 몇 분인지 구하는 식을 쓰세요.
minutes = 184 // 60

# (4) left를 분으로 묶고 마지막에 남는 초를 구하는 식을 쓰세요.
seconds = 4

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
