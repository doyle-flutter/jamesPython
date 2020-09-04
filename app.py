### Python 문법(입문)

# 변수
name = "james"
print(name)

# String
dataSt = 'Hi'
print(dataSt)
dataSt = "hi"
print(dataSt)
dataSt = ''' 
hi!'''
print(dataSt)

dataStLen = len(dataSt)
print(dataStLen) # 5

dataStIndexingSlice = dataSt[-1]
print(f'-1 : {dataStIndexingSlice}') # !
dataStIndexingSlice = dataSt[0:-1] # \n hi
print(f'0 ~ -2 : {dataStIndexingSlice}')

dataStSplit = dataSt.split()
print(dataStSplit)

# int , float , complex(복소수)
dataSt = 123
print(dataSt)
dataSt = 123.123
print(dataSt)
dataSt = 123.123-1j
print(dataSt)

# --------------------------- 
# 리스트(배열)
li = [1,2,3]
print( li ) # R

# - 리스트 인덱스 역순 가능
print( li[-2] )

# - 리스트 요소 길이
len( li ) # 기존 length 와 차이

# - 리스트 요소 삭제 D
del li[0] # del 키워드는 리스트 요소 외 적용 가능
print( li )

# - 리스트 요소 추가 C
li.append(4)
print( li )

# - 리스트 요소 변경 U
li[0] = 22
print( li )

# - map 고차함수
def aa(a):
    return a+1
li2 = list(map(aa,li))
print(li2)

# --------------------------- 
# 튜플(tuple) : 수정 불가능 한 리스트
tup = (1,2,3,3,3)
print(tup)

# --------------------------- 
# 집합(SET) : 중복을 허용하지 않는 리스트
ss = set(tup)
print(ss) # {1,2,3}

# --------------------------- 
# 사전(Dictionary) : 값에 이름(키)을 갖는 자료형
dic = {'key':'value'}
print(dic)
print(dic['key'])
print(len(dic))

# - dictionary & for
for k in dic:
    print(k)
    print(dic[k])

# - keys
print( list(dic.keys()) )

# - map 고차 함수 : key를 인자로 함
dicMapFunc = lambda k: dic[k]
dicMap = map( dicMapFunc, dic )
print( list(dicMap) )

# 함수
def fName():
	return "FUNC"
print(fName())

# 함수 인자 옵션 : 기본 값
# (1)
def argFunc1(a, b=3):
	return b

# (2)
def argFunc2(a=1,b=2):
	return b

# 주의 : 첫 인자만 기본 값 지정 불가능 기본 값을 지정하지 않았을 경우 맨 앞으로
# def argFunc3(a=1,b):
# 	return b

# 함수 인자의 개수를 자유롭게 사용할 경우
def argAny(*a):
	return a

argAny(1,2,3) # (1,2,3)
argAny(1,2) # (1,2)

def argAny2(a,*b):
	return b

print( argAny2(1,2,3) ) # (2,3)
print( argAny2(1,2,3,4,5) ) # (2,3,4,5)

# 키워드(네이밍) 옵션 : 순서를 무시 할 수 있음
aa = 123
bb = 321
def argName(a,b):
    return a+b

print(argName(b = bb, a = aa))

# 정의 되지 않은 키워드(네이밍) ** 
# 1 키워드를 적용하지 않을 경우 순서 중요
# 2 **key로 받은 인자의 타입 : <type 'dict'>
def customArg(a, b, **ab):
    return ab

print( customArg(custom1 = 12, custom2 = 1212,  a=1, b=2) ) 
# {'custom1': 12, 'custom2': 1212}

def customArg2(a, b, **ab):
    return ab

print( customArg2(10,20,custom123=123) ) # {'custom123': 123}
# 주의 : 키워드 옵션처럼 맨앞에서 사용 불가능
# print( customArg2(custom123=123,10,20) )

# 람다 Lambda : (익명함수) 사용 후 힙(heap) 메모리에서 증발
lamA = lambda a,b: a
print( lamA(a=3, b=4) ) # 3

# 반복문
for a in li2:
    print(a)

for a in li2[:2]:
    print(a)

# 제어문
for a in li2[:2]:
    if(a != 0):
        print("!0!0")
    print(a)
# 클래스 기본
class MyClass:
    # 생성자(constructor) : self -> Dart의 this를 의미하며
    # 생성자 및 메서드 등에서 첫 인자로 담아야 사용 가능
    # __NAME__ : 미리 생성 되어있는 특이한 이름의 규칙들
    def __init__(self, arg):
	# 생성시 초기화 할 수 있으며, self에 바인딩되어 변수를 별도 선언하지 않아도 됨
        self._arg = arg
    def myArg(self):
        return self._arg

myClass = MyClass(arg = "My Class !")
print( myClass.__class__ )
print( myClass.myArg() )


# @ : 데코레이터(정의된 키워드 또는 함수를 실행할 수 있음)

# 키워드 사용
# staticMethod & classMethod
class MyClass:
    a = 'CLS_Var'

    def __init__(self, arg):
        self._arg = arg

    def myArg(self):
        return self._arg

    @staticmethod
    def myStatic():
        return 'hi! Static'

    @classmethod
    def myClassM(cls,a):
        # cls에서는 self 키워드 사용 불가능
        return f'ClassVar : {cls.a} / ArgVar : {a}!'

# *주의 : 인스턴스 사용이 아니므로 클래스명 자체를 작성해야합니다
print( MyClass.myStatic() )
print( MyClass.myClassM(a='arg_Var') )

# 함수 및 클래스에서 데코레이터 사용
# Decorator Func
def myDeco(func):
    def deco():
        print("Hi Deco!")
        func()
        print("Bye Deco!!")
    return deco

@myDeco
def myFuncWithDeco():
    print("~ myFunction ~")

myFuncWithDeco()

# Decorator Class
class DecoClass:
		# 생성자
    def __init__(self, f):
        self.func = f
		# 호출
    def __call__(self, *args, **kwargs):
        print("DecoClass ~")
        self.func(*args, **kwargs)
        print(self.customInit(a="Deco Method ~"))

    def customInit(self,a):
        return a
# 클래스명을 입력. __call__ 을 통해 호출 됨
@DecoClass
def decoFunc():
    print("decoFunc ~")

decoFunc()

# Class Extends 
class PClass:
    def __init__(self, myName):
        self._myName = myName
    
    def __call__(self):
        self._pFunc()

    def _pFunc(self):
        print(f'Hi ! {self._myName} !!')

class CClass(PClass):
    def __init__(self, myName):
        PClass.__init__(self, myName)

pClass = PClass("James")
pClass() # __call__
cClass = CClass("James(inherit)")
cClass() # __call__

## 타입 지정
def com(p:PClass):
    p()
com(p=pClass)
 
# Class Implements : 패키지 사용 필요


