### 1장 파이선 입문을 위한 준비 <br />

▶ 파이선 설치와 에디터 <br />
. Python : https://www.python.org/downloads/ <br />
. PyCharm, VSCode <br />
. Thonny Python ( 라즈베리파이 기본 설치 ) <br />
. 파이선 설치확인: cmd >> python --version <br />

▶ vscode hello world <br />
. vscode 실행 ==> hello.py 파일 생성 >> python 버전확인 <br />
. 코드 실행: 우측 실행버튼 ( Run Python File ) <br />

▶ variable <br />
. print : 데이터 출력 <br />
. 숫자로 시작면 숫자 데이터, 문자로 시작하면 변수, 따움표로 시작하면 문자 <br />
. snake_case 방식으로 변수 이름( 권장 ) vs CapWord방식 (class는 CapWord) <br />

▶ 주석처리 <br />

- #: 한개의 라인 주석 <br />
- """ or ''' 멀티라인 주석 <br />
  ''' <br />
  multiline comment <br />
  second line comment <br />
  ''' <br />

▶ vscode 단축키 <br />

- 주석처리 : Ctrl + / <br />
- 멀티커서 : Ctrl + Alt 를 누르고 아래키 눌러서 멀티커서를 생성한다 > print를 입력 > Alt를 누르고 라인 끝을 클릭한다. > 괄호닫기를 입력한다. <br />
  3 print(3  
   3.14 print(3.14  
   -4 print(-4  
   -3.14 print(-3.14

### 2장 데이터 타입과 타입변환

▶ 데이터 타입 <br />

- 숫자형 ( int, float, complex )
- 글자형 ( 문자열, str )
- list : []
- tuple : (), list와 구조가 같고 수정이 불가
- set : {}, 값의 중복이 없다.
- dict ( dictionary ) : { key1 = value, key2= value2, ... }

#### 코드 블럭

```python
print (type(3))
print (type(3.3333333))
print (type("fdsdsfa"))
```

### 3장 입출력과 라이브러리(1)

- 파이선 입출력
- printf()함수: (\*values, sep=, end=)
- 문자열 포맷 : format()
- \ 문자
- input() 함수 : str로 받아진다.
- 파이선 라이브러리 : time, math, random, sys

### 4장 연산자와 조건문

- 사칙연산자, 비교연산자, 논리연산자
- 불리언 타입 (bool)
- 조건문
- 사칙연산자
  - // 몫, % 나머지, \*\* 거듭제곱
- 비교연산자

  - ==, !=, >, >=, <, >=

- 조건문
  - Block 문법 표기방법: 탭 1개 또는 Space 4개를 사용하여 Block 표시

### 5장 반복문과 제어 키워드

> 1. for 반복문, while 반복문
> 2. 제어 키워드: pass, break, continue
>
> > range( n )
> >
> > > range(3) : [0,1,2]  
> > > range(1,5) : [1,2,3,4]  
> > > range(1,10,2) : [1,3,5,7,9]

### 6장 함수

> 1. 함수선언
> 2. 함수의 매개변수, 인자 : 함수를 실행할 때 주는 것이 인자
> 3. 함수종료 및 반환
> 4. 함수영역

> > 함수선언
> >
> > > def 함수명( 매개변수1,2,...):

### 7장 데이터 타입의 함수

1. 빌트인 함수와 자료형 전용함수 차이
2. 파괴적인 함수 vs 비파괴적인 함수

### 8장 파일 객체와 with문

> 1. 목표
>    > - 파일객체 생성 및 읽기 : open(), close()
>    > - 파일객체 모드 : r, w, x, a, b, t, +
>    > - 안전한 파일 객체 처리를 위한 with

- r : raw string 형식

```
os.chdir(os.path.dirname(__file__))
open('02.txt', 'rt', encoding='utf-8')
print('{!r}'.format(fp2.readline()))
```

### 9장 변수 상태 저장, 오류 제어문

> 1. 목표
>    > - 파이선 객체 저장 ( pickle )
>    > - 오류 제어 : try.. except..finally

### 10장 파이선 표준 라이브러리

> 1. 목표
>    > - 시간 관련 datetime 라이브러리 학습
>    > - 시간 표현

```
date1 = now.strftime("%Y-%m-%d %H:%M:%S")
print( date1 )
```

###### 2024-12-19 15:19:35

https://www.youtube.com/watch?v=6J0lqMPi8AI

강사 추천 사이트
https://programmers.co.kr/
