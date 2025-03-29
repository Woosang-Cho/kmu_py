2025-01 KMU python
=============

1~4주차 강의록을 위주로 구성



## 1주차 - 프로그래밍을 배우는 이유
## 1.1. 프로그래밍을 배운다는 것

* 데이터 값의 저장,수치의 연산,메모리의 설정과 해제 등 개별 단위의 명령문을 체계적으로 조합하는 기술의 훈련

*  추상적인 논리 체계에 의거한 객체와 함수를 생성하고 정의하는 기술의 훈련
  

### 1.2. 실습 - ```print()``` 함수 활용

```python
#그냥 출력
printf('string')

#문자열 합하기는 그냥 + 붙이기
print('srting1' + 'string2')

#'' 안에 \n 넣으면 한 줄 띄어쓰기
print('string \n')
```

* python은 indent가 scope를 결정하는 무근본 언어이므로 주의

## 2주차 - ```input()``` 함수 활용, data types, ASCII, 

### 2.1.  ```input()``` 함수

```python
a = input('string')
```

* ```input()``` 안에 문자열을 받아서 변수 ```a```에 넣은거임

### 2.2. ```input()``` 과 ```print()``` 함께 이용

```python
name = input("What's your name?")
print('Hi' + name + '?')
```
* 이름을 받으면 인사해주는 코드
* 변수 이름은 숫자로 시작할 수 없다. 
* 과학적 표기법이나 언어 내 parsing 문제 때문이다.
*  숫자로 시작하려면 underbar( _ ) 달고 쓰자. ```_1var``` 처럼.


### 2.3. 실습 - 닉네임 제조기

week2 폴더 내 ```nick_maker.py``` 참고

### 2.4. Data types 

* Text types: ```str```
* Numeric types: ```int, float, complex```
* Sequence types: ```list, tuple, range```
* Set types: ```set, frozenset```
* Boolean type: ```bool```
* Binary types: ```bytes, bytearry, memorybiew```

python은 자동으로 변수를 인식한다. 다만 필요에 따라 강제로 변환 가능하다. 

### 2.5. 실습 - date types

필요에 따라 강제 type 변환이 가능하다

1. ```int``` 이용
```python
x = int("2019")
y = int("2000")

type(x-y)

>>> <clsss 'int'>
```
"string"인데 ```int``` 안에 넣어서 강제로 자료형이 바뀜.

```python
x = "2019"
y = "2000"
int(x) - int(y)
>>> 19

type(x)
>>> <clsss 'str'>
```

2. ```float``` 이용
```python
r = "5.5"
pi = "3.14"

float(r)*float(r)*float(pi)
```

"string"인데도 ```float```을 써서 강제로 실수형으로 변환함.

### 2.6. ASCII(American Standard code for Information Interchange)

* motivation: 컴퓨터에는 0, 1의 binary만 입력 가능하다. 숫자의 경우 진법 변환을 이용하지만, 글자의 경우는 어떻게 할까?

* 글자를 숫자로 mapping 하는 규칙을 만들자

* ASCII: 1Byte(128개 정보)를 이용해 mapping한다

### 2.7. 실습 - ASCII in python

* ```ord("string")``` : 해당 문자에 대응하는 ASCII를 반환한다
* ```chr(number)``` : 해당 숫자에 대응하는 ASCII를 반환한다

```python
ord("a")
>>> 97

ord(65)
>>> 'A'
```

* ```bin(number)``` : 10진수 숫자를 넣으면 대응하는 binary를 반환함
```python
bin(97)
>>> '0b1100001'
```