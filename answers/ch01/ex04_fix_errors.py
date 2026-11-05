# 1장 문제 4 정답
#
# 해설: 실수 3개
# 1. 2번째 print 앞의 띄어쓰기 → IndentationError: unexpected indent
#    줄 앞의 쓸데없는 띄어쓰기를 지워요.
# 2. pritn → NameError: name 'pritn' is not defined. Did you mean: 'print'?
#    print로 고쳐요.
# 3. '안내문이에요 의 닫는 따옴표가 없음 → SyntaxError: unterminated string literal
#    따옴표를 닫아요.
#
# 에러는 한 번에 하나씩만 보여 줄 때가 많아요. 하나 고치고 다시 실행하고, 또 고치고...
# 이렇게 반복하는 게 정상이에요.

print('에러는')
print('친절한')
print('안내문이에요')
