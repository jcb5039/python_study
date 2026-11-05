# 8장 문제 1 정답
#
# 해설:
# - 첫 줄의 N은 개수인데, 리스트로 받으면 len()으로 알 수 있어서 사실 안 써도 돼요.
#   그래도 입력의 첫 줄이니까 input()으로 읽어서 넘겨야 해요. (안 읽으면 둘째 줄을 N으로 읽게 돼요)
# - min(), max()로 바로 구해요.
#
# 직접 구현해 보기 (7장 "패턴 3"):
#   smallest = nums[0]
#   biggest = nums[0]
#   for x in nums:
#       if x < smallest:
#           smallest = x
#       if x > biggest:
#           biggest = x
#   → 음수가 있을 수 있으니 0이 아니라 첫 번째 값으로 시작해요.

n = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))
