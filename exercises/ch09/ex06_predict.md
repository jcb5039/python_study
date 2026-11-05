# 9장 문제 6: 결과 예측하기

코드를 **실행하지 말고** 결과를 먼저 적어 보세요. 그다음 직접 실행해서 확인하세요.

## 1번

```python
def double(n):
    return n * 2

print(double(3) + double(4))
```

내 예측:

## 2번

```python
def double(n):
    print(n * 2)

x = double(3)
print(x)
```

내 예측:

## 3번

```python
def hello():
    print('안녕')

print('시작')
```

내 예측:

## 4번

```python
def f(n):
    if n > 10:
        return '크다'
    print('여기 도착')
    return '작다'

print(f(20))
print(f(5))
```

내 예측:

## 5번

```python
def total(nums):
    s = 0
    for x in nums:
        s += x
        return s

print(total([1, 2, 3]))
```

내 예측 (힌트: return의 들여쓰기 위치를 보세요):

## 6번

```python
def greet(name, msg='안녕'):
    return f'{msg}, {name}'

print(greet('민지'))
print(greet('민지', '반가워'))
```

내 예측:

## 7번

```python
def swap(a, b):
    return b, a

x, y = swap(1, 2)
print(x, y)
```

내 예측:

---

틀린 문제가 있으면 **왜 틀렸는지 한 줄로** 적어 두세요.
