# 8장: 리스트

> **이 장의 목표:** 여러 값을 리스트에 담아서 꺼내고, 추가하고, 정렬하고, 합계·최댓값을 구할 수 있다.

학생 30명의 점수를 저장하려면 변수 30개(`score1`, `score2`, ...)를 만들어야 할까요? **리스트**를 쓰면 변수 하나에 전부 담을 수 있어요. 코딩테스트 입력은 대부분 "숫자 N개"라서 리스트는 반드시 알아야 해요.

---

## 1. 리스트 만들기

대괄호 `[ ]` 안에 값을 쉼표로 나눠서 넣어요.

```python
scores = [80, 95, 70]
names = ['민지', '철수', '영희']
empty = []
print(scores)
print(names)
print(empty)
```

```
[80, 95, 70]
['민지', '철수', '영희']
[]
```

리스트는 **칸이 나뉜 기차**라고 생각하면 돼요. 칸마다 값이 하나씩 타고 있고, 칸에는 0번부터 번호가 붙어 있어요.

```
값:     80    95    70
번호:    0     1     2
```

> 💡 4장에서 `split()`의 결과로 이미 리스트를 봤어요. `'a b c'.split()` → `['a', 'b', 'c']`

---

## 2. 꺼내기: 인덱스와 슬라이싱

4장 문자열과 **완전히 같은 방법**이에요.

```python
nums = [3, 1, 4, 1, 5]
print(nums[0])      # 첫 번째
print(nums[-1])     # 마지막
print(nums[1:3])    # 1번, 2번
print(len(nums))    # 개수
```

```
3
5
[1, 4]
5
```

없는 번호를 쓰면 `IndexError`가 나는 것도 같아요.

### 문자열과 다른 점: 리스트는 바꿀 수 있어요

문자열은 글자 하나를 바꿀 수 없었지만, 리스트는 **칸의 값을 바꿀 수 있어요.**

```python
nums = [1, 2, 3]
nums[0] = 10
print(nums)
```

```
[10, 2, 3]
```

---

## 3. 추가하고 빼기

| 쓰는 법 | 하는 일 |
| --- | --- |
| `리스트.append(값)` | **맨 뒤에** 추가 |
| `리스트.insert(번호, 값)` | 그 번호 자리에 끼워 넣기 |
| `리스트.pop()` | **맨 뒤** 값을 빼서 돌려줌 |
| `리스트.pop(번호)` | 그 번호의 값을 빼서 돌려줌 |
| `리스트.remove(값)` | 그 값을 찾아서 (처음 나오는 하나) 지움 |

```python
nums = [3, 1, 4]
nums.append(9)
print(nums)
nums.insert(0, 7)
print(nums)
last = nums.pop()
print(last, nums)
nums.remove(1)
print(nums)
```

```
[3, 1, 4, 9]
[7, 3, 1, 4, 9]
9 [7, 3, 1, 4]
[7, 3, 4]
```

> 💡 `append`가 가장 많이 쓰여요. **빈 리스트를 만들고 반복문에서 `append`로 채우는** 모양을 꼭 기억하세요.

```python
evens = []
for i in range(1, 11):
    if i % 2 == 0:
        evens.append(i)
print(evens)
```

```
[2, 4, 6, 8, 10]
```

### 문자열 메서드와 다른 점

4장에서 `s.upper()`는 원래 문자열을 바꾸지 않고 새 문자열을 돌려준다고 했죠? 리스트의 `append`, `insert`, `remove`, `sort`는 반대로 **원래 리스트를 직접 바꿔요.** 그래서 결과를 다시 담을 필요가 없어요.

```python
nums = [1, 2]
nums.append(3)        # ✅ nums가 직접 바뀜
print(nums)

nums = nums.append(4) # ❌ append는 아무것도 돌려주지 않아서(None) nums가 None이 돼요
print(nums)
```

```
[1, 2, 3]
None
```

---

## 4. 리스트에 쓰는 기본 기능

| 쓰는 법 | 결과 | 예 (`nums = [3, 1, 4, 1, 5]`) |
| --- | --- | --- |
| `len(nums)` | 개수 | `5` |
| `sum(nums)` | 합계 | `14` |
| `max(nums)` | 가장 큰 값 | `5` |
| `min(nums)` | 가장 작은 값 | `1` |
| `값 in nums` | 들어 있는지 | `4 in nums` → `True` |
| `nums.count(값)` | 그 값이 몇 개인지 | `nums.count(1)` → `2` |
| `nums.index(값)` | 그 값이 처음 나오는 번호 | `nums.index(4)` → `2` |

7장에서 반복문으로 직접 만든 합계, 최댓값을 **한 줄로** 구할 수 있어요.

```python
scores = [80, 95, 70]
print(sum(scores) / len(scores))    # 평균
```

```
81.66666666666667
```

> ⚠️ 빈 리스트에 `max()`, `min()`을 쓰면 `ValueError`가 나요. 빈 리스트에 `sum()`은 `0`이에요.

---

## 5. 정렬하기

| 쓰는 법 | 원래 리스트 | 돌려주는 것 |
| --- | --- | --- |
| `sorted(nums)` | **그대로** | 정렬된 **새 리스트** |
| `nums.sort()` | **직접 정렬됨** | 없음 (`None`) |

```python
nums = [3, 1, 4, 1, 5]
new_nums = sorted(nums)
print(new_nums)
print(nums)          # 그대로

nums.sort()
print(nums)          # 직접 바뀜
```

```
[1, 1, 3, 4, 5]
[3, 1, 4, 1, 5]
[1, 1, 3, 4, 5]
```

**큰 것부터(내림차순)** 정렬하려면 `reverse=True`를 넣어요.

```python
print(sorted([3, 1, 2], reverse=True))
```

```
[3, 2, 1]
```

> 💡 원래 순서도 필요하면 `sorted()`, 원래 순서가 필요 없으면 `sort()`를 써요. 헷갈리면 `sorted()`를 쓰면 안전해요.

문자열 리스트는 **가나다/ABC 순서**로 정렬돼요.

---

## 6. 반복문으로 돌기

`for`는 리스트의 값을 **앞에서부터 하나씩** 꺼내 줘요. 7장에서 문자열을 한 글자씩 돈 것과 같아요.

```python
scores = [80, 95, 70]
for s in scores:
    print(s)
```

```
80
95
70
```

**번호도 필요할 때**는 `range(len(리스트))`를 써요.

```python
names = ['민지', '철수', '영희']
for i in range(len(names)):
    print(i, names[i])
```

```
0 민지
1 철수
2 영희
```

> 11장에서 이걸 더 편하게 하는 `enumerate`를 배워요.

---

## 7. 코딩테스트 입력을 리스트로 받기

5장에서 "개수를 모르는 입력은 8장에서 배운다"고 했어요. 바로 이거예요.

### 한 줄에 숫자 여러 개

```
5
3 1 4 1 5
```

```python
n = int(input())
nums = list(map(int, input().split()))
print(nums)
```

```
[3, 1, 4, 1, 5]
```

`map(int, ...)`의 결과를 `list()`로 감싸면 리스트가 돼요. **이 줄도 꼭 외워 두세요.** 5장의 `a, b = map(...)`과 함께 코딩테스트 입력의 90%를 해결해요.

> 💡 `list()`로 감싸지 않고 `print(map(...))`을 하면 `<map object at 0x...>`처럼 이상한 글자가 나와요. `map`은 리스트가 아니라서, 리스트로 만들어야 번호로 꺼내거나 여러 번 쓸 수 있어요.

### 한 줄에 숫자 하나씩, N줄

```
3
10
20
30
```

```python
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(nums)
```

```
[10, 20, 30]
```

---

## 8. 리스트를 출력 모양에 맞추기

리스트를 그냥 `print`하면 대괄호와 쉼표가 같이 나와요. 코딩테스트는 보통 **띄어쓰기로 나눈 모양**을 원해요.

```python
nums = [1, 2, 3]
print(nums)                         # [1, 2, 3]
print(*nums)                        # 1 2 3
print(' '.join(map(str, nums)))     # 1 2 3
```

- `print(*nums)`: 앞의 `*`는 리스트를 **풀어서** 하나씩 넣어 줘요. `print(1, 2, 3)`과 같아져요.
- `' '.join(...)`: 4장의 `join`은 **문자열**만 합칠 수 있어서, `map(str, ...)`으로 먼저 글자로 바꿔요.

둘 다 결과는 같아요. 처음에는 `print(*nums)`가 쉬워요.

---

## 9. 자주 하는 실수

| 실수 | 결과 | 고친 모습 |
| --- | --- | --- |
| `nums = nums.append(4)` | `nums`가 `None` | `nums.append(4)` |
| `nums = nums.sort()` | `nums`가 `None` | `nums.sort()` 또는 `nums = sorted(nums)` |
| `nums[len(nums)]` | `IndexError` | 마지막은 `nums[-1]` |
| `list(map(int, input()))` (split 빠짐) | 한 글자씩 쪼개짐 | `input().split()` |
| `print(nums)` 그대로 제출 | `[1, 2, 3]` 모양이라 오답 | `print(*nums)` |
| `' '.join(nums)` (숫자 리스트) | `TypeError` | `' '.join(map(str, nums))` |
| `nums.remove(9)` (없는 값) | `ValueError` | `if 9 in nums:`로 먼저 확인 |

---

## 10. 이 장의 문제

문제 폴더: `exercises/ch08/`. **judge.py로 채점**해요.

| 파일 | 내용 |
| --- | --- |
| `ex01_min_max.py` | 최솟값과 최댓값 |
| `ex02_average.py` | 평균과 평균 넘는 사람 수 |
| `ex03_smaller_than.py` | X보다 작은 수만 출력 |
| `ex04_sort.py` | 정렬해서 출력 |
| `ex05_second_largest.py` | 두 번째로 큰 수 |
| `ex06_predict.md` | 결과 예측하기 |

---

## 11. 체크리스트

- [ ] 리스트를 만들고 번호로 꺼낼 수 있다
- [ ] 빈 리스트를 만들고 반복문에서 `append`로 채울 수 있다
- [ ] `len`, `sum`, `max`, `min`, `in`을 쓸 수 있다
- [ ] `sorted()`와 `.sort()`의 차이를 설명할 수 있다
- [ ] 내림차순으로 정렬할 수 있다
- [ ] `list(map(int, input().split()))`로 한 줄의 숫자들을 리스트로 받을 수 있다
- [ ] 리스트를 `1 2 3` 모양으로 출력할 수 있다

다음 장: [9장: 함수](ch09_functions.md)
