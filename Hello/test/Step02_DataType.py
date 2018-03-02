#-*- coding:utf-8 -*-

# int type (정수)
num1 = 10

# float type (실수)
num2 = 10.1

# bool type (논리)
isRun = True
isWait = False
isGreater = 10>5

# str type (문자)
myName ='kimgura'
yourName = 'monkey'

# unicode type (한글을 다룰때는 unicode type 을 써야한다)
ourName=u'에이콘'
ourName2=u"에이콘 아카데미"

#list type
nums=[10, 20, 30, 40, 50] # int type 을 저장하고 있는 list
names=['kim', 'lee', 'park'] # str type 을 저장하고 있는 list
friends=[u'김구라', u'해골', u'원숭이'] # unicode type 을 저장

# tuple type (list type 의 read only 버전)
nums2=(10, 20, 30, 40, 50)
names2=('kim', 'lee', 'park')
friends2=(u'김구라', u'해골', u'원숭이')

# dict type
mem1={"num":1, "name":u"김구라", "isMan":True}
mem2={"num":2, "name":u"해골", "isMan":False}

# function type (범위를 나타내는 중괄호를 쓰지 않는다.)
def a():
    pass #pass 는 빈 공간을 의미한다.

def b():
    print 'one'
    print 'two'
    print 'three'

# b 라는 함수 호출
b()

# b 함수의 참조값을 c 에 대입
c=b

# None type
emptyVar=None # java 의 null 이라고 이해 하면 된다.

# set type (집합, 묶음) 단, 중복을 허용하지 않는다.
set1 = {10, 20, 30, 10, 20}

#python 은 기본 데이터 type 이 존재하지 않는다. 모두 참조 데이터이다!

print "Step02_DataType.py 가 종료됩니다."