#-*- coding:utf-8 -*-
'''
    1. 함수도 객체다
    2. 함수도 변수에 담을 수 있다.
    3. 함수도 다른 함수를 호출하면서 인자로 전달할 수 있다.
    4. 함수가 리턴값이 함수 일수도 있다.
'''

# 1.
def f1():
    pass

def f2():
    pass

# 함수의 참조값(id값) 출력해 보기
print 'id(f1) :', id(f1)
print 'id(f2) :', id(f2)

# 2.

def gura():
    print "i am gura!"
    
a=gura # 함수의 참조값을 다른 변수에 담을 수 있다.

print "id(gura) :", id(gura)
print "id(a) :", id(a)

# 3.
def test(arg):
    arg()
    
test(gura) # 함수를 call 하면서 함수의 참조값 전달하기

# 4.

def getAction():
    #함수를 만들어서
    def sing():
        print "노래를 불러요!"
    #함수의 참조값 리턴
    return sing

# getAction() 함수가 리턴해주는 값을 변수에 담기
result = getAction()
# result 에 담긴 값은 function type 이므로 호출할 수 있다.
result()
