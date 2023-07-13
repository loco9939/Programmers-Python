# 리스트 생성

```py
odd = []
even = list()
sample = [1,3,4,5]
ex = [1,'안녕',True, [3,4],{'name':'yiju'}]
```

# 인덱싱

```py
ex[-1] # {'name':'yiju'}
```

# 슬라이싱 (변수[start, end, interval])

## 마지막 인덱싱은 포함하지 않는다.

```py
string = 'abcdefghijk'

sample[0:2] # [1,3]
string[0:4:2] # ac
```

# 리스트 연산

```py
arr1 = [1,2]
arr2 = [3,4]

arr3 = arr1 + arr2 # [1,2,3,4]
arr4 = arr1 * 3 # [1,2,1,2,1,2]
```

# 리스트 메서드

## insert(index,elem)

```py
test = [1,3,4]
test.insert(1,2) # [1,2,3,4]
```

## del a[index]

```py
test1 = [1,3,2,3,4]
del test1[1] # [1,2,3,4]
del test1[:2] # [3,4]
```

## clear()

```py
test2 = [1,2,3,4]
test2.clear() # []
```

## remove(elem)

### 처음 나온 원소값 하나만 제거

```py
test3 = [1,3,4,5]
test3.remove(4) # [1,3,5]
```

## sort(), sorted()

```py
test4 = [2,1,4,3]
test4.sort() # 원본 배열 수정
sorted(test4) # 원본 유지, 정렬된 배열 반환

test4.sort(reverse=True) # [4,3,2,1]
```

## reverse(), reversed()

### 내림차순 정렬이 아닌 배열을 거꾸로 뒤집는 것

```py
test5 = [1,4,5,6]
test5.reverse()

reversed(test5) # <list_reverseiterator object at 0x7f9e7d917ca0>
```

### reversed()는 객체를 반환한다.

```py
list(reversed(test5)) # [6,5,4,1]
```

# 리스트 복사하기 copy()

## 참조값을 복사하기 때문에 얕은 복사이다.

```py
a = [1,10,20]
b = a

a == b # True
a is b # True

```

## 깊은 복사

```py
import copy
c = [5,15,20]
d = copy.deepcopy(c)

c == d # True => c,d의 값은 같다.
c is d # False => c, d가 같지는 않다.
```
