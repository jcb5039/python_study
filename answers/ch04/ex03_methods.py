# 4장 문제 3 정답
#
# 해설:
# - strip(): 양 끝의 공백만 지워요. 가운데 띄어쓰기는 그대로.
# - cleaned.upper(): 메서드는 원래 문자열을 바꾸지 않고 새 문자열을 돌려줘요.
# - count('a'): 개수, replace('a', 'o'): 전부 바꾸기
# - '@' in email: 들어 있으면 True
# - find('@'): 처음 나오는 번호. r-u-n-n-e-r 가 0~5번이라 '@'는 6번
# - email[:at_index]: 0번부터 at_index 바로 앞까지 → 'runner'
#   다른 풀이: email.split('@')[0]

raw = '   Hello Python   '
fruit = 'banana'
email = 'runner@test.com'

cleaned = raw.strip()
loud = cleaned.upper()
a_count = fruit.count('a')
changed = fruit.replace('a', 'o')
has_at = '@' in email
at_index = email.find('@')
user_id = email[:at_index]

# ───── 채점 코드 ─────
# 여기부터는 채점용이에요. 지금은 읽지 않아도 돼요. (9장에서 배우는 '함수'로 만들었어요)

def check(label, actual, expected):
    if type(actual) == type(expected) and actual == expected:
        print(f'✅ {label}')
    else:
        print(f'❌ {label}  결과: {actual!r}  기대: {expected!r}')

check('cleaned', cleaned, 'Hello Python')
check('loud', loud, 'HELLO PYTHON')
check('a_count', a_count, 3)
check('changed', changed, 'bonono')
check('has_at', has_at, True)
check('at_index', at_index, 6)
check('user_id', user_id, 'runner')
