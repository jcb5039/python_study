# 8장 문제 5 정답
#
# 해설:
# - sorted(nums, reverse=True)로 큰 순서 새 리스트를 만들면 [1]번이 두 번째로 큰 수예요.
# - 위치는 원래 리스트(nums)에서 찾아야 해요. sorted()는 nums를 바꾸지 않으니까 그대로 남아 있어요.
#   nums.sort()를 썼다면 원래 순서가 사라져서 위치를 찾을 수 없어요!
# - index()는 0부터 세니까 1번째부터 세려면 + 1
#
# 다른 풀이 (정렬 없이, 7장 "패턴 3" 응용):
#   first = 가장 큰 수, second = 두 번째로 큰 수 를 기억하면서 한 번만 돌아요.
#   새 값 x가 first보다 크면 → second = first, first = x
#   아니고 second보다 크면  → second = x
#   N이 아주 클 때 정렬보다 빨라요.

n = int(input())
nums = list(map(int, input().split()))

second = sorted(nums, reverse=True)[1]
position = nums.index(second) + 1
print(second, position)
