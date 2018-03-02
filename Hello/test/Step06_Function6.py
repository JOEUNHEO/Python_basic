#-*- coding:utf-8 -*-
'''
    함수의 리턴값
'''

def test1():
    print "test1()"

r1=test1()

# None 이 리턴 되는 함수
def test2():
    print "test2()"
    return None

r2=test2()

# int type 이 리턴되는 함수
def test3():
    print "test3()"
    return 10

r3=test3()

# dict type 을 리턴해주는 함수
def test4():
    print "test4()"
    return {"num":999}

r4=test4()

# list type 을 리턴해 주는 함수
def test5():
    print "test5()"
    names=['kim', 'park', 'lee']
    return names

r5=test5()

# function type 을 리턴해주는 함수
def test6():
    print "test6()"
    def a():
        print "a()"
    return a

r6=test6()

r6()

print "Step06_Function^.py 가 종료 됩니다."