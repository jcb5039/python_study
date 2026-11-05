# 11장: 리스트 응용

> **이 장의 목표:** 리스트를 짧고 편하게 다루는 파이썬 도구들(리스트 컴프리헨션, `enumerate`, `zip`, 2차원 리스트, 정렬 기준)을 쓸 수 있다.

이 장에서 배우는 건 **새로운 능력이라기보다 지름길**이에요. 7~8장의 반복문으로 다 할 수 있는 일이지만, 이 도구들을 쓰면 코드가 짧아지고 실수가 줄어요. 코딩테스트 풀이를 볼 때도 자주 나와서, 알아야 남의 코드를 읽을 수 있어요.

---

## 1. 리스트 컴프리헨션: 한 줄로 리스트 만들기

8장에서 이렇게 리스트를 만들었어요.

```python
squares = []
for x in range(1, 6):
    squares.append(x * x)
print(squares)
```

**리스트 컴프리헨션**을 쓰면 한 줄이에요.

```python
squares = [x * x for x in range(1, 6)]
print(squares)
```

```
[1, 4, 9, 16, 25]
```

### 읽는 법

```python
[x * x  for x in range(1, 6)]
 ─────  ────────────────────
 담을 것     어디서 꺼낼지
```

> "`range(1, 6)`에서 `x`를 하나씩 꺼내서, **`x * x`를 담은** 리스트"

뒤에서부터 읽으면 쉬워요. **for 부분을 먼저** 읽고, 그다음 앞의 **담을 것**을 읽어요.

### 조건 붙이기

뒤에 `if`를 붙이면 **조건에 맞는 것만** 담아요.

```python
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)
```

```
[2, 4, 6, 8, 10]
```

원래 모양과 나란히 놓고 보면 이래요.

```python
evens = []
for x in range(1, 11):        # ← for 부분
    if x % 2 == 0:            # ← if 부분
        evens.append(x)       # ← 담을 것
```

### 자주 쓰는 예

```python
words = ['apple', 'kiwi']
print([w.upper() for w in words])                    # 전부 대문자로
print([int(x) for x in '1 2 3'.split()])             # 글자를 숫자로 (map 대신)
print([len(w) for w in words])                       # 길이들
```

```
['APPLE', 'KIWI']
[1, 2, 3]
[5, 4]
```

> 💡 `list(map(int, input().split()))`과 `[int(x) for x in input().split()]`은 같은 결과예요. 편한 쪽을 쓰면 돼요.

> ⚠️ 너무 길어지면 오히려 읽기 어려워요. 한 줄에 안 들어갈 만큼 복잡하면 그냥 `for`문으로 쓰세요.

---

## 2. `enumerate`: 번호와 값을 같이

8장에서 번호가 필요하면 `range(len(...))`를 썼어요.

```python
names = ['민지', '철수']
for i in range(len(names)):
    print(i, names[i])
```

`enumerate`를 쓰면 **번호와 값을 한 번에** 받아요.

```python
names = ['민지', '철수']
for i, name in enumerate(names):
    print(i, name)
```

```
0 민지
1 철수
```

번호를 1부터 시작하고 싶으면 `start=1`을 넣어요.

```python
for i, name in enumerate(names, start=1):
    print(f'{i}등 {name}')
```

```
1등 민지
2등 철수
```

---

## 3. `zip`: 두 리스트를 나란히

길이가 같은 두 리스트를 **같은 번호끼리 짝지어** 돌 수 있어요. 지퍼(zip)의 양쪽 이가 하나씩 맞물리는 모양이에요.

```python
names = ['민지', '철수']
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)
```

```
민지 90
철수 85
```

> 💡 길이가 다르면 **짧은 쪽에 맞춰서** 멈춰요.

---

## 4. 2차원 리스트: 표 만들기

리스트 안에 리스트를 넣으면 **표(행과 열)**를 만들 수 있어요. 엑셀 시트나 바둑판을 생각하면 돼요.

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
]
print(grid[1][2])
print(len(grid), len(grid[0]))
```

```
6
2 3
```

- `grid[1]`: 1번 **줄(행)** → `[4, 5, 6]`
- `grid[1][2]`: 1번 줄의 2번 **칸(열)** → `6`
- `len(grid)`: 줄 수, `len(grid[0])`: 한 줄의 칸 수

```
         열0  열1  열2
행0  →  [ 1,   2,   3 ]
행1  →  [ 4,   5,   6 ]
```

### 표 전체 돌기

```python
for row in grid:
    print(*row)
```

```
1 2 3
4 5 6
```

**모든 칸**을 하나씩 보려면 반복문을 두 번(7장 중첩) 써요.

```python
total = 0
for row in grid:
    for x in row:
        total += x
print(total)
```

```
21
```

### 줄마다 합계

```python
print([sum(row) for row in grid])
```

```
[6, 15]
```

### ⚠️ 빈 표를 만들 때 함정

0으로 채운 2줄 3칸 표를 만들고 싶어요. 이렇게 하면 **안 돼요.**

```python
bad = [[0] * 3] * 2
bad[0][0] = 1
print(bad)
```

```
[[1, 0, 0], [1, 0, 0]]
```

`[0, 0, 0]` 줄 **하나를 두 번 가리킨** 거라서, 한 줄을 바꾸면 다른 줄도 같이 바뀌어요. 리스트 컴프리헨션으로 **줄마다 새로** 만들어야 해요.

```python
good = [[0] * 3 for _ in range(2)]
good[0][0] = 1
print(good)
```

```
[[1, 0, 0], [0, 0, 0]]
```

> 이 함정은 경력 있는 사람도 가끔 빠져요. **"2차원은 컴프리헨션으로 만든다"**고 외워 두세요.

### 코딩테스트 입력으로 표 받기

```
2 3        ← 줄 수, 칸 수
1 2 3
4 5 6
```

```python
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
```

---

## 5. 정렬 기준 정하기: `key`

8장의 `sorted()`는 값 자체의 크기로 정렬했어요. **"무엇을 기준으로"** 정렬할지 정하고 싶으면 `key`를 써요.

```python
words = ['banana', 'kiwi', 'apple']
print(sorted(words, key=len))
```

```
['kiwi', 'apple', 'banana']
```

`key=len`은 "각 값에 `len`을 해 본 결과로 비교해"라는 뜻이에요. 그래서 **길이 순**으로 정렬됐어요.

### `lambda`: 그 자리에서 만드는 작은 함수

기준이 `len`처럼 이미 있는 함수가 아니면, `lambda`로 **이름 없는 작은 함수**를 그 자리에서 만들어요.

```python
words = ['banana', 'kiwi', 'apple']
print(sorted(words, key=lambda w: w[-1]))     # 마지막 글자 기준
```

```
['banana', 'apple', 'kiwi']
```

`lambda w: w[-1]`은 9장의 이 함수와 같아요.

```python
def last_char(w):
    return w[-1]
```

> `lambda 매개변수: 돌려줄 값` (return을 안 쓰고, 한 줄만 돼요)

### (이름, 점수) 정렬하기

```python
students = [('철수', 85), ('영희', 90), ('민지', 90)]
print(sorted(students, key=lambda s: s[1], reverse=True))
```

```
[('영희', 90), ('민지', 90), ('철수', 85)]
```

`s[1]`은 점수예요. 점수가 높은 순서로 정렬됐어요.

### 기준 두 개: 점수가 같으면 이름 순

점수가 같은 영희와 민지는 원래 순서대로 남아 있어요. "점수가 같으면 **이름 가나다순**"으로 하고 싶으면 기준을 **튜플로 두 개** 줘요.

```python
print(sorted(students, key=lambda s: (-s[1], s[0])))
```

```
[('민지', 90), ('영희', 90), ('철수', 85)]
```

- 튜플은 **첫 번째 값으로 먼저** 비교하고, 같으면 두 번째 값으로 비교해요.
- `-s[1]`: 점수에 마이너스를 붙여서 **높은 점수가 앞**으로 오게 해요. (`reverse=True`를 쓰면 이름까지 거꾸로 돼서 이렇게 해요)
- `s[0]`: 점수가 같으면 이름 오름차순

코딩테스트의 "정렬 문제"는 거의 다 이 모양이에요.

---

## 6. 자주 하는 실수

| 실수 | 결과 | 고친 모습 |
| --- | --- | --- |
| `[x for x in range(5) if x % 2 == 0 else 0]` | `SyntaxError` | 거르기만 할 땐 `if`만. 값을 바꿀 땐 `[x if x % 2 == 0 else 0 for x in range(5)]` |
| `for i, x in names:` (enumerate 빠짐) | 에러 | `for i, x in enumerate(names):` |
| `[[0] * m] * n` | 줄이 같이 바뀜 | `[[0] * m for _ in range(n)]` |
| `grid[열][행]` 순서 헷갈림 | 엉뚱한 칸 | `grid[행][열]` (줄 먼저) |
| `sorted(words, key=len())` | `TypeError` | `key=len` (괄호 없이 함수 이름만) |
| 점수 내림차순 + 이름 오름차순에 `reverse=True` | 이름도 거꾸로 | `key=lambda s: (-s[1], s[0])` |

---

## 7. 이 장의 문제

문제 폴더: `exercises/ch11/`. 파일을 그냥 실행하면 채점돼요.

| 파일 | 내용 |
| --- | --- |
| `ex01_comprehension.py` | 리스트 컴프리헨션 연습 |
| `ex02_enumerate_zip.py` | 번호 붙이기, 두 리스트 짝짓기 |
| `ex03_grid.py` | 2차원 리스트 다루기 |
| `ex04_sort_key.py` | 기준을 정해서 정렬하기 |
| `ex05_predict.md` | 결과 예측하기 |

---

## 8. 체크리스트

- [ ] `[x * 2 for x in nums if x > 0]`을 읽고 `for`문으로 바꿔 쓸 수 있다
- [ ] `enumerate`로 번호와 값을 같이 받을 수 있다
- [ ] `zip`으로 두 리스트를 짝지어 돌 수 있다
- [ ] `grid[행][열]`로 2차원 리스트의 칸을 꺼낼 수 있다
- [ ] 빈 2차원 리스트를 올바르게 만들 수 있다
- [ ] `sorted(..., key=lambda ...)`로 기준을 정해 정렬할 수 있다
- [ ] "점수 높은 순, 같으면 이름 순" 정렬을 쓸 수 있다

다음 장: [12장: 코딩테스트 실전](ch12_coding_test.md)
