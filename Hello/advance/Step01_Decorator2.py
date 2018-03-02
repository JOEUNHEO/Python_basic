#-*- coding:utf-8 -*-
'''
    decorator 는 함수의 장식자 이다.
'''

# decorator 로 사용할 함수 정의하기
def helloBye(func):
    # 인자로 전달된 func 에는 장식된 함수의 참조값이 전달 된다.
    def wrapper():
        print "hello!"
        func() # 장식된 함수를 호출하는 부분
        print "bye~"
    return wrapper

# f1 함수를 helloBye decorator 함수로 장식하기
@helloBye
def f1():
    print "f1() 수행됨"
        
@helloBye
def f2():
    print "f2() 수행됨"
    
@helloBye
def f3():
    print "f3() 수행됨"
    

f1()
f2()
f3()
