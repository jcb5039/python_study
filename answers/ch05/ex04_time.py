# 5장 문제 4 정답
#
# 해설:
# - 숫자 하나를 받으니까 int(input())
# - 분은 60으로 나눈 몫, 초는 60으로 나눈 나머지
# - '6분 15초' 모양은 f-string으로 만들어요.
#
# 자주 틀리는 점:
# - print(minutes, '분', rest, '초') 는 '6 분 15 초' 처럼 칸이 생겨서 틀려요.

seconds = int(input())
minutes = seconds // 60
rest = seconds % 60
print(f'{minutes}분 {rest}초')
