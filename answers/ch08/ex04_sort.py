# 8장 문제 4 정답
#
# 해설:
# - 한 줄에 하나씩이니까 빈 리스트 + 반복문 + append(int(input()))
# - sorted(nums): 오름차순 새 리스트
# - sorted(nums, reverse=True): 내림차순 새 리스트
# - sorted()는 원래 nums를 바꾸지 않으니 두 번 써도 괜찮아요.
#
# 자주 틀리는 점:
# - list(map(int, input().split()))로 받으면 첫 숫자 하나만 읽고 끝나요.
# - print(nums.sort()) → None 이 출력돼요. sort()는 아무것도 돌려주지 않아요.

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

print(*sorted(nums))
print(*sorted(nums, reverse=True))
