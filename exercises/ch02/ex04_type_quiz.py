# 2장 문제 4: 자료형 맞히기
#
# 각 값의 자료형 이름을 글자로 적으세요. 'int', 'float', 'str', 'bool' 중 하나예요.
#   예: q0의 값 7은 정수니까 → q0 = 'int'
#
# 실행해 보기 전에 머릿속으로 먼저 답을 정하세요. type()으로 확인하는 건 채점 후에!
#
# 채점: python3 exercises/ch02/ex04_type_quiz.py
# 힌트: 강의 2장 "헷갈리기 쉬운 것들"

q0 = 'int'    # 7          (예시, 이미 채워져 있어요)
q1 = None     # 3.0
q2 = None     # '3.0'
q3 = None     # False
q4 = None     # -15
q5 = None     # ''
q6 = None     # 'True'
q7 = None     # int('8')
q8 = None     # str(8)
q9 = None     # 10 / 2      ← 3장에서 배울 내용을 살짝 미리 봐요. 일단 찍어 보세요!

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('q0 (7)', q0, type(7).__name__)
check('q1 (3.0)', q1, type(3.0).__name__)
check("q2 ('3.0')", q2, type('3.0').__name__)
check('q3 (False)', q3, type(False).__name__)
check('q4 (-15)', q4, type(-15).__name__)
check("q5 ('')", q5, type('').__name__)
check("q6 ('True')", q6, type('True').__name__)
check("q7 (int('8'))", q7, type(int('8')).__name__)
check('q8 (str(8))', q8, type(str(8)).__name__)
check('q9 (10 / 2)', q9, type(10 / 2).__name__)
