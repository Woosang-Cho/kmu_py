2025-01 KMU python
=============

1~4주차 강의록을 위주로 구성

- [2025-01 KMU python](#2025-01-kmu-python)
  - [1주차 - 프로그래밍을 배우는 이유](#1주차---프로그래밍을-배우는-이유)
    - [1.1. 프로그래밍을 배운다는 것](#11-프로그래밍을-배운다는-것)
    - [1.2. 실습 - `print()` 함수 활용](#12-실습---print-함수-활용)
  - [2주차 - `input()` 함수 활용, data types, ASCII,](#2주차---input-함수-활용-data-types-ascii)
    - [2.1.  `input()` 함수](#21--input-함수)
    - [2.2. `input()` 과 `print()` 함께 이용](#22-input-과-print-함께-이용)
    - [2.3. 실습 - 닉네임 제조기](#23-실습---닉네임-제조기)
    - [2.4. Data types](#24-data-types)
    - [2.5. 실습 - date types](#25-실습---date-types)
    - [2.6. ASCII(American Standard code for Information Interchange)](#26-asciiamerican-standard-code-for-information-interchange)
    - [2.7. 실습 - ASCII in python](#27-실습---ascii-in-python)
  - [3주차 - 알고리즘의 개념](#3주차---알고리즘의-개념)
    - [3.1. 알고리즘의 정의](#31-알고리즘의-정의)
    - [3.2. 변수 형식 변경(type casting)](#32-변수-형식-변경type-casting)
    - [3.3. 실습 - 두 자리 수의 자리수 별 숫자의 합](#33-실습---두-자리-수의-자리수-별-숫자의-합)
    - [3.4. 실습 - 여행 경비 더치페이 계산기](#34-실습---여행-경비-더치페이-계산기)
  - [4주차 - 프로그래밍의 주요 개념 및 도구](#4주차---프로그래밍의-주요-개념-및-도구)
    - [4.1. 프로그래밍의 과정](#41-프로그래밍의-과정)
    - [4.2. 실습 - BMI 계산기](#42-실습---bmi-계산기)


## 1주차 - 프로그래밍을 배우는 이유
### 1.1. 프로그래밍을 배운다는 것

* 데이터 값의 저장,수치의 연산,메모리의 설정과 해제 등 개별 단위의 명령문을 체계적으로 조합하는 기술의 훈련

*  추상적인 논리 체계에 의거한 객체와 함수를 생성하고 정의하는 기술의 훈련
  

### 1.2. 실습 - `print()` 함수 활용

```python
#그냥 출력
printf('string')

#문자열 합하기는 그냥 + 붙이기
print('srting1' + 'string2')

#'' 안에 \n 넣으면 한 줄 띄어쓰기
print('string \n')
```

* python은 indent가 scope를 결정하는 무근본 언어이므로 주의

## 2주차 - `input()` 함수 활용, data types, ASCII, 

### 2.1.  `input()` 함수

```python
a = input('string')
```

* `input()` 안에 문자열을 받아서 변수 `a`에 넣은거임

### 2.2. `input()` 과 `print()` 함께 이용

```python
name = input("What's your name?")
print('Hi' + name + '?')
```
* 이름을 받으면 인사해주는 코드
* 변수 이름은 숫자로 시작할 수 없다. 
* 과학적 표기법이나 언어 내 parsing 문제 때문이다.
*  숫자로 시작하려면 underbar( _ ) 달고 쓰자. `_1var` 처럼.


### 2.3. 실습 - 닉네임 제조기

week2 폴더 내 `nick_maker.py` 참고

### 2.4. Data types 

* Text types: `str`
* Numeric types: `int, float, complex`
* Sequence types: `list, tuple, range`
* Set types: `set, frozenset`
* Boolean type: `bool`
* Binary types: `bytes, bytearry, memorybiew`

python은 자동으로 변수를 인식한다. 다만 필요에 따라 강제로 변환 가능하다. 

### 2.5. 실습 - date types

필요에 따라 강제 type 변환이 가능하다

1. `int` 이용
```python
x = int("2019")
y = int("2000")

type(x-y)

>>> <clsss 'int'>
```
"string"인데 `int` 안에 넣어서 강제로 자료형이 바뀜.

```python
x = "2019"
y = "2000"
int(x) - int(y)
>>> 19

type(x)
>>> <clsss 'str'>
```

2. `float` 이용
```python
r = "5.5"
pi = "3.14"

float(r)*float(r)*float(pi)
```

"string"인데도 `float`을 써서 강제로 실수형으로 변환함.

### 2.6. ASCII(American Standard code for Information Interchange)

* motivation: 컴퓨터에는 0, 1의 binary만 입력 가능하다. 숫자의 경우 진법 변환을 이용하지만, 글자의 경우는 어떻게 할까?

* 글자를 숫자로 mapping 하는 규칙을 만들자

* ASCII: 1Byte(128개 정보)를 이용해 mapping한다

### 2.7. 실습 - ASCII in python

* `ord("string")` : 해당 문자에 대응하는 ASCII를 반환한다
* `chr(number)` : 해당 숫자에 대응하는 ASCII를 반환한다

```python
ord("a")
>>> 97

ord(65)
>>> 'A'
```

* `bin(number)` : 10진수 숫자를 넣으면 대응하는 binary를 반환함
```python
bin(97)
>>> '0b1100001'
```

## 3주차 - 알고리즘의 개념

### 3.1. 알고리즘의 정의
* 문제 해결을 위해 입력을 토대로 원하는 출력을 유도하는 규칙의 집합.
*  경로, 추천, 분배 등 
*  연습: 숫자 맞추기 게임(?), 경로 찾기

### 3.2. 변수 형식 변경(type casting)

예를 들어 변수 a와 b에 저장된 숫자를 더할 때, `input()`이 string type이면 숫자 계산이 안되므로, type casting이 필요함.

### 3.3. 실습 - 두 자리 수의 자리수 별 숫자의 합

* 3주차의 `digit.py` 파일 참고.


### 3.4. 실습 - 여행 경비 더치페이 계산기

* 3주차 파일의 `travel_cost.py` 참고
* `fstring`과 `round`를 잘 활용하면 좋다.

## 4주차 - 프로그래밍의 주요 개념 및 도구
키워드? 
### 4.1. 프로그래밍의 과정

문제 정의 &rarr; 해결 방법 설계 &rarr; 코딩 &rarr; 프로그램 검증 &rarr; 문서화 및 유지보수

### 4.2. 실습 - BMI 계산기

* https://github.com/Woosang-Cho/BMI_calculator.git 참고
* 또는 4주차 `bmi_calculator.py` 참고
* 조건문을 이용


