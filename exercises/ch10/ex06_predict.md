# 10장 문제 6: 결과 예측하기

코드를 **실행하지 말고** 결과를 먼저 적어 보세요. 그다음 직접 실행해서 확인하세요.

## 1번

```python
d = {'a': 1, 'b': 2}
d['c'] = 3
d['a'] = 10
print(d)
print(len(d))
```

내 예측:

## 2번

```python
d = {'x': 5}
print(d.get('y', 0) + d.get('x', 0))
```

내 예측:

## 3번

```python
d = {'사과': 3, '귤': 5}
print('사과' in d, 3 in d)
```

내 예측:

## 4번

```python
counts = {}
for n in [1, 2, 1, 1, 3]:
    counts[n] = counts.get(n, 0) + 1
print(counts[1], len(counts))
```

내 예측:

## 5번

```python
s = set([4, 4, 2, 4, 2])
print(len(s), sorted(s))
```

내 예측:

## 6번

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(sorted(a & b), sorted(a - b))
```

내 예측:

## 7번

```python
x = {}
print(type(x))
```

내 예측 (dict일까요, set일까요?):

## 8번

```python
d = {'a': 1, 'b': 2}
total = 0
for k in d:
    total += d[k]
print(total)
```

내 예측:

---

틀린 문제가 있으면 **왜 틀렸는지 한 줄로** 적어 두세요.
