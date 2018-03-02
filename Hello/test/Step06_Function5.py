#-*- coding:utf-8 -*-
'''
    함수를 호출할 때 전달하는 keyword 인자를 dict 로 받을 수 있다.
'''

# kwargs : keyword arguments 의 약자
def test1(**kwargs):
    print kwargs

test1()
test1(num=1)
test1(num=2, name="haegol")
test1(num=3, name="monkey", addr="zoo")

# 오류 발생 (keyword 인자가 아니므로)
#test1("one", "two")

print "------------------------------------"

# 어떤 형태의 호출도 다 받아 줄 수 있는 형태의 함수
def test2(*args, **kwargs):
    print args, kwargs
    
test2()
test2(10, 20, num=1, name="kim")
test2(11, 12, 13)
test2(num=2, name="park")